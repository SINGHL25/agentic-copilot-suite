# Agentic Copilot Suite 🤖

A multi-agent AI system to automate daily corporate tasks:
- ✉️ Email replies
- 🗓️ Calendar updates
- 📅 Meeting summaries
- 📋 Task tracking

## Features
- Built in Python with OpenAI, Google API, Whisper
- Modular agents for easy extensibility

## Quick Start
```bash
pip install -r requirements.txt
python main.py
```

## Agents
- `EmailAgent`: Summarizes and replies to emails
- `CalendarAgent`: Reads upcoming calendar events
- `MeetingAgent`: Transcribes + summarizes audio

## .env Setup
```
OPENAI_API_KEY=your_key_here
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
```

## Coming Soon
- Slack summarizer agent
- Notion sync
- Streamlit dashboard

## License
MIT