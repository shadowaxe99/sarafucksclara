```python
# sara_ai/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AI Model
GPT3_MODEL = os.getenv('GPT3_MODEL')

# API Keys
API_KEYS = {
    'gmail': os.getenv('GMAIL_API_KEY'),
    'google_calendar': os.getenv('GOOGLE_CALENDAR_API_KEY'),
    'google_tasks': os.getenv('GOOGLE_TASKS_API_KEY'),
    'microsoft_graph': os.getenv('MICROSOFT_GRAPH_API_KEY'),
    'microsoft_outlook_calendar': os.getenv('MICROSOFT_OUTLOOK_CALENDAR_API_KEY'),
    'microsoft_to_do': os.getenv('MICROSOFT_TO_DO_API_KEY'),
    'zoom': os.getenv('ZOOM_API_KEY')
}
```