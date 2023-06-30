import socketio
import time

class SwapGGInterface:
    def __init__(self, url, authorizationToken, session):
        self.socket = socketio.Client()
        self.url = url
        self.authorizationToken = authorizationToken
        self.session = session
        self.screenshot_ready = False
        self.currentItem = None

        self.socket.on('screenshot:ready', self.onScreenshotReady)

    def onScreenshotReady(self, data):
        if hasattr(self.currentItem, "inspectLink"):
            self.currentItem.inspectLink = self.currentItem.inspectLink.replace("%20", " ")
            if str(data['inspectLink']) == self.currentItem.inspectLink:
                self.screenshot_ready = True

    def waitForScreenshot(self, CsWeapon):
        # jest to jedyne rozwiązanie które nie wykorzystuje 90% procesora
        while self.screenshot_ready == False:
            time.sleep(1)
        #ustawienie flagi na następny przedmiot
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
        return self.session.post(url=url, json=data, headers=headers)

    def createScreenshot(self, CsWeapon):
        r = self.fetchScreenshotInfo(CsWeapon)
        if r.status_code == 200:
            if r.json()['result']['state'] == 'COMPLETED':
                CsWeapon.screenshotLink, CsWeapon.item_float = r.json()['result']['imageLink'], str(r.json()['result']["itemInfo"]["floatvalue"])[:9]
            elif r.json()['result']['state'] == 'IN_QUEUE':
                #cekaj aż w odpowiedzi z websocketa pojawi się odpowiedni inspectlink
                CsWeapon = self.waitForScreenshot(self.currentItem)

        self.currentItem = None
        return CsWeapon