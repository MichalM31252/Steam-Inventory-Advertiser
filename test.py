import requests
import socketio

class SocketIOClient:
    def __init__(self, url, authorization_token):
        self.socket = socketio.Client()
        self.url = url
        self.authorization_token = authorization_token

        self.socket.on('screenshot:ready', self.on_screenshot_ready)


    def connect(self):
        self.socket.connect(self.url)

    def on_screenshot_ready(self, data):
        print(data)

    def on_message(self, message):
        print(message)

    def createScreenshot(self):
        url = "https://market-api.swap.gg/v1/screenshot"
        data = {
            "inspectLink": "steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M4298170983645466406A29388074428D16888506045285984669"
        }
        headers = {
            'Content-type': 'application/json',
            'Authorization': self.authorization_token
        }
        requests.post(url=url, json=data, headers=headers)

# Example usage
client = SocketIOClient('https://market-ws.swap.gg', '#')
client.connect()
client.createScreenshot()
