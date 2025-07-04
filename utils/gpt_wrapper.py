import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_email(text):
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize and draft polite reply:\n{text}"}]
    )['choices'][0]['message']['content']

def summarize_meeting_transcript(transcript):
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize this meeting:\n{transcript}"}]
    )['choices'][0]['message']['content']