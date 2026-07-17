# ==========================================
# AI VIDEO LANGUAGE STUDIO - STREAMLIT APP
# PART 1
# ==========================================

import streamlit as st
import os
import tempfile


# Import utility functions
from utils.audio import extract_audio
from utils.speech import speech_to_text
from utils.translate import translate_text
from utils.tts import generate_voice
from utils.subtitles import create_subtitle
from utils.video import create_video
from utils.helpers import save_uploaded_file


# ==========================================
# STREAMLIT PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Video Language Studio",
    page_icon="🎬",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("🎬 AI Video Language Studio")

st.write(
    """
    Upload a video and create a translated AI version.

    Features:
    - 🎧 Extract Audio
    - 📝 Speech To Text
    - 🌍 Translation
    - 🔊 AI Voice Generation
    - 📄 Subtitle Creation
    - 🎥 Recreated Video
    """
)


# ==========================================
# CREATE FOLDERS
# ==========================================

folders = [
    "uploads",
    "outputs",
    "temp"
]


for folder in folders:

    if not os.path.exists(folder):

        os.makedirs(folder)



# ==========================================
# SIDEBAR SETTINGS
# ==========================================

st.sidebar.header(
    "⚙ Settings"
)


languages = {

    "English":"en",

    "Hindi":"hi",

    "Spanish":"es",

    "French":"fr",

    "German":"de",

    "Japanese":"ja",

    "Chinese":"zh",

    "Arabic":"ar"

}



language_name = st.sidebar.selectbox(

    "Translate Video Into",

    list(languages.keys())

)



language = languages[language_name]



st.sidebar.info(

    "Select target language and upload your video"

)



# ==========================================
# VIDEO UPLOAD
# ==========================================

st.header(
    "📤 Upload Video"
)


uploaded_video = st.file_uploader(

    "Choose Video File",

    type=[
        "mp4",
        "mov",
        "avi",
        "mkv"
    ]

)



if uploaded_video:


    st.video(
        uploaded_video
    )


    st.success(
        "Video uploaded successfully"
    )



# ==========================================
# PROCESS BUTTON
# ==========================================


process_button = st.button(

    "🚀 Start AI Video Processing"

)
# ==========================================
# PART 2 : VIDEO PROCESSING PIPELINE
# ==========================================


def process_video(video_path, target_language):

    # ------------------------------
    # Extract Audio
    # ------------------------------

    st.info("🎧 Extracting audio...")

    audio_path = extract_audio(
        video_path
    )

    st.success(
        "Audio extracted successfully"
    )


    # ------------------------------
    # Speech To Text
    # ------------------------------

    st.info(
        "📝 Converting speech to text..."
    )


    transcript = speech_to_text(
        audio_path
    )


    st.success(
        "Speech converted successfully"
    )


    st.subheader(
        "Original Transcript"
    )


    st.text_area(

        "Original Text",

        transcript,

        height=200

    )


    # ------------------------------
    # Translation
    # ------------------------------

    st.info(
        "🌍 Translating text..."
    )


    translated_text = translate_text(

        transcript,

        target_language

    )


    st.success(
        "Translation completed"
    )


    st.subheader(
        "Translated Text"
    )


    st.text_area(

        "Translated Text",

        translated_text,

        height=200

    )


    # ------------------------------
    # AI Voice Generation
    # ------------------------------

    st.info(
        "🔊 Generating AI Voice..."
    )


    voice_path = generate_voice(

        translated_text,

        target_language

    )


    st.success(
        "AI voice generated"
    )



    # ------------------------------
    # Subtitle Creation
    # ------------------------------

    st.info(
        "📄 Creating subtitles..."
    )


    subtitle_path = create_subtitle(

        translated_text

    )


    st.success(
        "Subtitle created"
    )



    # ------------------------------
    # Create Final Video
    # ------------------------------

    st.info(
        "🎬 Creating final video..."
    )


    final_video = create_video(

        video_path,

        voice_path,

        subtitle_path

    )


    st.success(
        "Final video created successfully"
    )


    return (

        final_video,

        subtitle_path,

        transcript,

        translated_text

    )



# ==========================================
# PROCESS BUTTON ACTION
# ==========================================


if process_button:


    if uploaded_video is None:


        st.warning(

            "Please upload a video first"

        )


    else:


        with st.spinner(

            "AI processing started..."

        ):


            video_path = save_uploaded_file(

                uploaded_video

            )


            output_video, subtitle, original, translated = process_video(

                video_path,

                language

            )


            st.session_state["video"] = output_video

            st.session_state["subtitle"] = subtitle

            st.session_state["original"] = original

            st.session_state["translated"] = translated
# ==========================================
# PART 3 : OUTPUT DISPLAY & DOWNLOAD
# ==========================================


if "video" in st.session_state:


    st.divider()


    st.header(
        "🎥 Final AI Generated Video"
    )


    final_video = st.session_state["video"]


    # Video Preview

    st.video(
        final_video
    )



    # Download Video

    with open(

        final_video,

        "rb"

    ) as file:


        st.download_button(

            label="⬇ Download Final Video",

            data=file,

            file_name="AI_Translated_Video.mp4",

            mime="video/mp4"

        )



    st.divider()



    # Subtitle Download

    st.header(
        "📄 Subtitle Download"
    )


    subtitle_file = st.session_state["subtitle"]


    with open(

        subtitle_file,

        "rb"

    ) as file:


        st.download_button(

            label="⬇ Download Subtitle (.srt)",

            data=file,

            file_name="subtitle.srt",

            mime="text/plain"

        )



    st.divider()



    # Transcript Display

    st.header(
        "📝 Transcript"
    )


    st.subheader(
        "Original Speech"
    )


    st.text_area(

        "Original",

        st.session_state["original"],

        height=200

    )



    st.subheader(
        "Translated Speech"
    )


    st.text_area(

        "Translated",

        st.session_state["translated"],

        height=200

    )



# ==========================================
# FOOTER
# ==========================================

st.divider()


st.caption(

    "AI Video Language Studio | Built with Streamlit + Whisper + AI Voice"

)
