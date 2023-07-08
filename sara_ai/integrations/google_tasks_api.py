```python
import google.auth
from googleapiclient.discovery import build

# Load the API keys
from sara_ai.config import API_KEYS

# Load the Task schema
from sara_ai.schemas import Task

def create_task(task: Task):
    credentials, _ = google.auth.default()
    service = build('tasks', 'v1', credentials=credentials)
    result = service.tasks().insert(tasklist='@default', body=task.dict()).execute()
    return result['id']

def update_task(task: Task):
    credentials, _ = google.auth.default()
    service = build('tasks', 'v1', credentials=credentials)
    result = service.tasks().update(tasklist='@default', task=task.id, body=task.dict()).execute()
    return result['id']

def delete_task(task_id: str):
    credentials, _ = google.auth.default()
    service = build('tasks', 'v1', credentials=credentials)
    service.tasks().delete(tasklist='@default', task=task_id).execute()
    return task_id
```