from agents.email_agent import run_email_agent
from agents.calendar_agent import run_calendar_agent
from agents.meeting_agent import run_meeting_agent

if __name__ == "__main__":
    run_email_agent()
    run_calendar_agent()
    run_meeting_agent("data/transcripts/meeting1.mp3")