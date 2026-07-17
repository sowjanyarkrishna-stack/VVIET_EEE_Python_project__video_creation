# ==========================================
# translate.py
# Text Translation Module
# ==========================================

from deep_translator import GoogleTranslator



def translate_text(text, target_language):

    """
    Translate text into selected language

    Input:
        text -> original transcript
        target_language -> language code

    Output:
        translated text
    """

    translator = GoogleTranslator(

        source="auto",

        target=target_language

    )


    translated = translator.translate(

        text

    )


    return translated
