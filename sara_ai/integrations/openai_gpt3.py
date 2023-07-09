```python
import openai
from sara_ai.config import API_KEYS

GPT3_MODEL = "text-davinci-003"

def integrate_gpt3():
    openai.api_key = API_KEYS['openai']

def generate_response(prompt):
    response = openai.Completion.create(
        engine=GPT3_MODEL,
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
```