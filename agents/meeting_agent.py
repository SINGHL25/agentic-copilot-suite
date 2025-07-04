import whisper
from utils.gpt_wrapper import summarize_meeting_transcript

def run_meeting_agent(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    summary = summarize_meeting_transcript(result['text'])
    print(summary)