```python
import google.auth
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

def authenticate_google_calendar():
    creds, _ = google.auth.default()
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
    try:
        service = build('calendar', 'v3', credentials=creds)
        return service
    except Exception as e:
        print(e)
        return None

def schedule_appointment(user, appointment):
    service = authenticate_google_calendar()
    if service:
        event = {
            'summary': appointment['title'],
            'start': {
                'dateTime': appointment['start_time'],
                'timeZone': user['time_zone'],
            },
            'end': {
                'dateTime': appointment['end_time'],
                'timeZone': user['time_zone'],
            },
        }
        try:
            event = service.events().insert(calendarId='primary', body=event).execute()
            return event['id']
        except Exception as e:
            print(e)
            return None

def reschedule_appointment(user, appointment_id, new_time):
    service = authenticate_google_calendar()
    if service:
        try:
            event = service.events().get(calendarId='primary', eventId=appointment_id).execute()
            event['start']['dateTime'] = new_time['start_time']
            event['end']['dateTime'] = new_time['end_time']
            updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
            return updated_event['id']
        except Exception as e:
            print(e)
            return None

def view_appointment(user, appointment_id):
    service = authenticate_google_calendar()
    if service:
        try:
            event = service.events().get(calendarId='primary', eventId=appointment_id).execute()
            return event
        except Exception as e:
            print(e)
            return None
```