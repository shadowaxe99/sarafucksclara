```python
from sara_ai.integrations.google_tasks_api import GoogleTasksAPI
from sara_ai.integrations.microsoft_to_do_api import MicrosoftToDoAPI

class TaskManagement:
    def __init__(self, user):
        self.user = user
        self.google_tasks_api = GoogleTasksAPI(API_KEYS['google'])
        self.microsoft_to_do_api = MicrosoftToDoAPI(API_KEYS['microsoft'])

    def create_task(self, task):
        if self.user.preference == 'google':
            response = self.google_tasks_api.create_task(task)
        else:
            response = self.microsoft_to_do_api.create_task(task)
        return TASK_CREATED, response

    def update_task(self, task_id, updates):
        if self.user.preference == 'google':
            response = self.google_tasks_api.update_task(task_id, updates)
        else:
            response = self.microsoft_to_do_api.update_task(task_id, updates)
        return TASK_UPDATED, response

    def delete_task(self, task_id):
        if self.user.preference == 'google':
            response = self.google_tasks_api.delete_task(task_id)
        else:
            response = self.microsoft_to_do_api.delete_task(task_id)
        return TASK_DELETED, response

    def set_reminder(self, task_id, reminder_time):
        if self.user.preference == 'google':
            response = self.google_tasks_api.set_reminder(task_id, reminder_time)
        else:
            response = self.microsoft_to_do_api.set_reminder(task_id, reminder_time)
        return TASK_REMINDER_SET, response
```