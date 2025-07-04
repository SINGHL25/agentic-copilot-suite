from utils.email_utils import read_unread_emails, send_email_reply
from utils.gpt_wrapper import summarize_email

def run_email_agent():
    emails = read_unread_emails()
    for email in emails:
        summary = summarize_email(email['body'])
        reply = f"Hi {email['sender_name']},\n\n{summary}\n\nRegards"
        send_email_reply(email['thread_id'], reply)