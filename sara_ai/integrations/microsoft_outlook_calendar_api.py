```python
import requests
from sara_ai.config import API_KEYS

class MicrosoftOutlookCalendarAPI:
    def __init__(self):
        self.base_url = "https://graph.microsoft.com/v1.0/me/calendar"
        self.headers = {
            "Authorization": f"Bearer {API_KEYS['MICROSOFT_GRAPH']}",
            "Content-Type": "application/json"
        }

    def schedule_appointment(self, start_time, end_time, subject, attendees):
        data = {
            "subject": subject,
            "start": {
                "dateTime": start_time,
                "timeZone": "UTC"
            },
            "end": {
                "dateTime": end_time,
                "timeZone": "UTC"
            },
            "attendees": [{"emailAddress": {"address": attendee}} for attendee in attendees]
        }
        response = requests.post(self.base_url, headers=self.headers, json=data)
        return response.json()

    def reschedule_appointment(self, appointment_id, new_start_time, new_end_time):
        data = {
            "start": {
                "dateTime": new_start_time,
                "timeZone": "UTC"
            },
            "end": {
                "dateTime": new_end_time,
                "timeZone": "UTC"
            }
        }
        response = requests.patch(f"{self.base_url}/{appointment_id}", headers=self.headers, json=data)
        return response.json()

    def view_appointment(self, appointment_id):
        response = requests.get(f"{self.base_url}/{appointment_id}", headers=self.headers)
        return response.json()
```