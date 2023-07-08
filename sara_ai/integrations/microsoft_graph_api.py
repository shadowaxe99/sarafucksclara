```python
import requests
from sara_ai.config import API_KEYS

class MicrosoftGraphAPI:
    def __init__(self):
        self.base_url = "https://graph.microsoft.com/v1.0"
        self.token = API_KEYS['MICROSOFT_GRAPH']

    def draft_email(self, recipient, subject, content):
        url = f"{self.base_url}/me/messages"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        data = {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": "Text",
                    "content": content
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": recipient
                        }
                    }
                ]
            },
            "saveToSentItems": "false"
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def send_email(self, message_id):
        url = f"{self.base_url}/me/messages/{message_id}/send"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers)
        return response.status_code

    def schedule_email(self, recipient, subject, content, send_time):
        url = f"{self.base_url}/me/messages"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }
        data = {
            "message": {
                "subject": subject,
                "body": {
                    "contentType": "Text",
                    "content": content
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": recipient
                        }
                    }
                ]
            },
            "schedule": {
                "sendAt": send_time
            },
            "saveToSentItems": "true"
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()
```