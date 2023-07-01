import socketio
import time
from requests import request

class SwapGGInterface:
    def __init__(self, url, authorizationToken):
        self.socket = socketio.Client()
        self.url = url
        self.authorizationToken = authorizationToken
        self.screenshot_ready = False
        self.currentItem = None

        self.socket.on('screenshot:ready', self.onScreenshotReady)

    def onScreenshotReady(self, data):
        if hasattr(self.currentItem, "inspectLink"):
            self.currentItem.inspectLink = self.currentItem.inspectLink.replace("%20", " ")
            if str(data['inspectLink']) == self.currentItem.inspectLink:
                self.screenshot_ready = True

    def waitForScreenshot(self, CsWeapon):
        # this is the only solution that doesn't eat up 90% of the processing power
        while self.screenshot_ready == False:
            time.sleep(1)
        #reset the flag for the next screenshot
        self.screenshot_ready = False
        return self.createScreenshot(CsWeapon)

    def connect(self):
        self.socket.connect(self.url)

    def fetchScreenshotInfo(self, CsWeapon):
        self.currentItem = CsWeapon
        url = "https://market-api.swap.gg/v1/screenshot"
        data = {
            "inspectLink": CsWeapon.inspectLink.replace("%20", " "),
        }
        headers = {
            'Content-type': 'application/json',
            'Authorization': self.authorizationToken
        }
        return self.request.post(url=url, json=data, headers=headers)

    def createScreenshot(self, CsWeapon):
        r = self.fetchScreenshotInfo(CsWeapon)
        if r.status_code == 200:
            if r.json()['result']['state'] == 'COMPLETED':
                CsWeapon.screenshotLink, CsWeapon.item_float = r.json()['result']['imageLink'], str(r.json()['result']["itemInfo"]["floatvalue"])[:9]
            elif r.json()['result']['state'] == 'IN_QUEUE':
                #wait untill a correct inspectlink is returned
                CsWeapon = self.waitForScreenshot(self.currentItem)

        self.currentItem = None
        return CsWeapon