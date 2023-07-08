```python
import requests
from sara_ai.config import API_KEYS

class ZoomAPI:
    def __init__(self):
        self.base_url = "https://api.zoom.us/v2"
        self.headers = {
            "Authorization": f"Bearer {API_KEYS['ZOOM']}",
            "Content-Type": "application/json"
        }

    def schedule_meeting(self, user_id, meeting_details):
        endpoint = f"{self.base_url}/users/{user_id}/meetings"
        response = requests.post(endpoint, headers=self.headers, json=meeting_details)
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to schedule meeting: {response.text}")

    def update_meeting(self, meeting_id, meeting_details):
        endpoint = f"{self.base_url}/meetings/{meeting_id}"
        response = requests.patch(endpoint, headers=self.headers, json=meeting_details)
        if response.status_code == 204:
            return {"status": "success"}
        else:
            raise Exception(f"Failed to update meeting: {response.text}")

    def delete_meeting(self, meeting_id):
        endpoint = f"{self.base_url}/meetings/{meeting_id}"
        response = requests.delete(endpoint, headers=self.headers)
        if response.status_code == 204:
            return {"status": "success"}
        else:
            raise Exception(f"Failed to delete meeting: {response.text}")

zoom_api = ZoomAPI()
```
