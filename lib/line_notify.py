import os 
import requests

class line_notify:
    def __init__(self) -> None:
        self.token = os.environ.get("Line_TOKEN")

    def send_msg(self, msg):

        headers = { "Authorization": "Bearer " + self.token }
        data = { 'message': msg }

        try:
            requests.post("https://notify-api.line.me/api/notify",
                headers = headers, data = data)

        except Exception :
            return None