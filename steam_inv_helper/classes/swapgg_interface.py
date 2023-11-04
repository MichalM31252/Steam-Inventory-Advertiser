import socketio
import time
import requests
from typing import Union


class SwapGGInterface:
    def __init__(self, url, authorization_token):
        self.socket = socketio.Client()
        self.url = url
        self.authorization_token = authorization_token
        self.screenshot_ready = False
        self.current_item = None

        self.socket.on("screenshot:ready", self.on_screenshot_ready)

    def on_screenshot_ready(self, data) -> None:
        if hasattr(self.current_item, "inspect_link"):
            self.current_item.inspect_link = self.current_item.inspect_link.replace(
                "%20", " "
            )
            if str(data["inspectLink"]) == self.current_item.inspect_link:
                self.screenshot_ready = True

    def wait_for_screenshot(self) -> None:
        # this is the only solution that doesn't eat up 90% of the processing power
        while not self.screenshot_ready:
            time.sleep(1)
        # reset the flag for the next screenshot
        self.screenshot_ready = False

    def connect(self) -> None:
        self.socket.connect(self.url)

    def fetch_screenshot_info(self, CSWeapon):
        self.current_item = CSWeapon
        url = "https://api.swap.gg/v2/screenshot"
        data = {
            "inspectLink": CSWeapon.inspect_link.replace("%20", " "),
        }
        headers = {
            "Content-type": "application/json",
            "Authorization": self.authorization_token,
        }
        swapgg_response = requests.post(url=url, json=data, headers=headers).json()
        return swapgg_response if swapgg_response["status"] == "OK" else False

    def get_screenshot_status(self, swapgg_response) -> bool:
        screenshot_status = swapgg_response["result"]["state"]
        if screenshot_status == "COMPLETED":
            return True
        elif screenshot_status == "IN_QUEUE":
            return False
        else:
            raise TypeError(
                "The screenshot data was unusable because the status was equal to: {screenshot_status}"
            )
