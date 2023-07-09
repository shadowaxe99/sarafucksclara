```python
from datetime import datetime
from sara_ai.integrations.google_calendar_api import GoogleCalendarAPI
from sara_ai.integrations.microsoft_outlook_calendar_api import MicrosoftOutlookCalendarAPI
from sara_ai.integrations.zoom_api import ZoomAPI

class ScheduleManagement:
    def __init__(self, user):
        self.user = user
        self.google_calendar = GoogleCalendarAPI()
        self.outlook_calendar = MicrosoftOutlookCalendarAPI()
        self.zoom = ZoomAPI()

    def schedule_appointment(self, title, start_time, end_time, attendees, location=None, description=None):
        if self.user.preference == 'Google':
            event = self.google_calendar.create_event(self.user, title, start_time, end_time, attendees, location, description)
        else:
            event = self.outlook_calendar.create_event(self.user, title, start_time, end_time, attendees, location, description)
        return 'APPOINTMENT_SCHEDULED', event

    def reschedule_appointment(self, event_id, new_start_time, new_end_time):
        if self.user.preference == 'Google':
            event = self.google_calendar.update_event(self.user, event_id, new_start_time, new_end_time)
        else:
            event = self.outlook_calendar.update_event(self.user, event_id, new_start_time, new_end_time)
        return 'APPOINTMENT_RESCHEDULED', event

    def view_appointment(self, event_id):
        if self.user.preference == 'Google':
            event = self.google_calendar.get_event(self.user, event_id)
        else:
            event = self.outlook_calendar.get_event(self.user, event_id)
        return 'APPOINTMENT_VIEWED', event

    def schedule_zoom_meeting(self, topic, start_time, duration, agenda=None):
        meeting = self.zoom.create_meeting(self.user, topic, start_time, duration, agenda)
        return 'ZOOM_MEETING_SCHEDULED', meeting
```