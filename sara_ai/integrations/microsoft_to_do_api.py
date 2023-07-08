```python
import requests
from sara_ai.config import API_KEYS

class MicrosoftToDoAPI:
    def __init__(self):
        self.base_url = "https://graph.microsoft.com/v1.0/me/todo/lists"
        self.headers = {
            "Authorization": f"Bearer {API_KEYS['MICROSOFT_TO_DO']}",
            "Content-Type": "application/json"
        }

    def create_task(self, task):
        url = f"{self.base_url}/tasks"
        data = {
            "title": task.title,
            "dueDateTime": {
                "dateTime": task.due_date,
                "timeZone": "UTC"
            },
            "reminderDateTime": {
                "dateTime": task.reminder_date,
                "timeZone": "UTC"
            }
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

    def update_task(self, task_id, task):
        url = f"{self.base_url}/tasks/{task_id}"
        data = {
            "title": task.title,
            "dueDateTime": {
                "dateTime": task.due_date,
                "timeZone": "UTC"
            },
            "reminderDateTime": {
                "dateTime": task.reminder_date,
                "timeZone": "UTC"
            }
        }
        response = requests.patch(url, headers=self.headers, json=data)
        return response.json()

    def delete_task(self, task_id):
        url = f"{self.base_url}/tasks/{task_id}"
        response = requests.delete(url, headers=self.headers)
        return response.status_code == 204
```