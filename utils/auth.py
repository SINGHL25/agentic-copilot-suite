from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_calendar_service():
    credentials = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=['https://www.googleapis.com/auth/calendar.readonly']
    )
    return build('calendar', 'v3', credentials=credentials)