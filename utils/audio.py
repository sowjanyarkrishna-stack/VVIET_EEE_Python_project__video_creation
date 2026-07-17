# ==========================================
# audio.py
# Extract Audio From Video
# ==========================================

import os
from moviepy.editor import VideoFileClip


def extract_audio(video_path):

    """
    Extract audio track from uploaded video

    Input:
        video_path -> video file path

    Output:
        audio file path
    """


    output_folder = "temp"


    if not os.path.exists(output_folder):

        os.makedirs(output_folder)



    audio_path = os.path.join(

        output_folder,

        "extracted_audio.wav"

    )


    # Load video

    video = VideoFileClip(video_path)



    # Extract audio

    audio = video.audio



    audio.write_audiofile(

        audio_path,

        codec="pcm_s16le"

    )



    # Close resources

    audio.close()

    video.close()



    return audio_path
