import socketio
import time
import requests


class SwapGGInterface:
    def __init__(self, url, authorization_token):
        self.socket = socketio.Client()
        self.url = url
        self.authorization_token = authorization_token
        self.screenshot_ready = False
        self.current_item = None

        self.socket.on("screenshot:ready", self.on_screenshot_ready)

    def on_screenshot_ready(self, data):
        if hasattr(self.current_item, "inspect_link"):
            self.current_item.inspect_link = self.current_item.inspect_link.replace(
                "%20", " "
            )
            if str(data["inspectLink"]) == self.current_item.inspect_link:
                self.screenshot_ready = True

    def wait_for_screenshot(self, CsWeapon, swapgg_response):
        # this is the only solution that doesn't eat up 90% of the processing power
        while not self.screenshot_ready:
            time.sleep(1)
        # reset the flag for the next screenshot
        self.screenshot_ready = False
        return self.get_screenshot(CsWeapon, swapgg_response)

    def connect(self):
        self.socket.connect(self.url)

    def fetch_screenshot_info(self, CsWeapon):
        self.current_item = CsWeapon
        url = "https://market-api.swap.gg/v1/screenshot"
        data = {
            "inspectLink": CsWeapon.inspect_link.replace("%20", " "),
        }
        headers = {
            "Content-type": "application/json",
            "Authorization": self.authorization_token,
        }
        res = requests.post(url=url, json=data, headers=headers)
        return res if res.status_code == 200 else False

    def get_screenshot(self, CsWeapon, swapgg_response):
        screenshot_status = swapgg_response.json()["result"]["state"]
        if screenshot_status == "COMPLETED":
            CsWeapon.screenshot_link, CsWeapon.item_float = (
                swapgg_response.json()["result"]["imageLink"],
                str(swapgg_response.json()["result"]["itemInfo"]["floatvalue"])[:9],
            )
        elif screenshot_status == "IN_QUEUE":
            # wait untill a correct inspect_link is returned
            CsWeapon = self.wait_for_screenshot(self.current_item, swapgg_response)
        self.current_item = None
        return CsWeapon
