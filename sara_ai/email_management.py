```python
from sara_ai.integrations.gmail_api import GmailAPI
from sara_ai.integrations.microsoft_graph_api import MicrosoftGraphAPI

class EmailManagement:
    def __init__(self, user):
        self.user = user
        if user.email_provider == 'gmail':
            self.email_api = GmailAPI(API_KEYS['gmail'])
        elif user.email_provider == 'outlook':
            self.email_api = MicrosoftGraphAPI(API_KEYS['outlook'])

    def draft_email(self, recipient, subject, body):
        email = {
            'recipient': recipient,
            'subject': subject,
            'body': body,
            'status': 'draft'
        }
        self.user.emails.append(email)
        return 'EMAIL_DRAFTED'

    def send_email(self, email):
        if email in self.user.emails and email['status'] == 'draft':
            self.email_api.send_email(email['recipient'], email['subject'], email['body'])
            email['status'] = 'sent'
            return 'EMAIL_SENT'
        else:
            return 'EMAIL_NOT_FOUND_OR_NOT_DRAFT'

    def schedule_email(self, email, send_time):
        if email in self.user.emails and email['status'] == 'draft':
            self.email_api.schedule_email(email['recipient'], email['subject'], email['body'], send_time)
            email['status'] = 'scheduled'
            return 'EMAIL_SCHEDULED'
        else:
            return 'EMAIL_NOT_FOUND_OR_NOT_DRAFT'
```