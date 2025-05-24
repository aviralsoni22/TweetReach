import os
from dotenv import load_dotenv

load_dotenv()

MOCK_API_URL = "http://localhost:3000"
MOCK_BEARER_TOKEN = "mock_bearer_token_123"

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("APP_PASSWORD")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")
