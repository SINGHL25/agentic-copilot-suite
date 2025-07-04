def read_unread_emails():
    # Dummy email list for testing
    return [{
        'sender_name': 'John',
        'body': 'Can you update me on the Q3 report?',
        'thread_id': '123456'
    }]

def send_email_reply(thread_id, reply):
    print(f"Sending reply to thread {thread_id}:\n{reply}\n")