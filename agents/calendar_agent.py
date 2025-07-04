from utils.auth import get_calendar_service
from datetime import datetime

def run_calendar_agent():
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'
    events = service.events().list(calendarId='primary', timeMin=now, maxResults=5).execute()
    for event in events['items']:
        print(f"{event['start'].get('dateTime')} → {event['summary']}")