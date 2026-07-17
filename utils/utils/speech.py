# ==========================================
# speech.py
# Speech To Text using Whisper AI
# ==========================================

import whisper


# Load Whisper model
# tiny = faster
# base = better accuracy
# small/medium = higher accuracy

model = whisper.load_model("base")



def speech_to_text(audio_path):

    """
    Convert audio into text

    Input:
        audio_path -> wav/mp3 audio file

    Output:
        transcript text
    """


    result = model.transcribe(
        audio_path
    )


    text = result["text"]


    return text
