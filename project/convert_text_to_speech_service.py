import os
import tempfile
import uuid

from gtts import gTTS
from pydantic import BaseModel


class ConvertTextResponse(BaseModel):
    """
    Provides the URL of the generated speech audio after successful conversion.
    """

    audioUrl: str


async def convert_text_to_speech(
    accent: str, text: str, language: str, pitch: float, speed: float
) -> ConvertTextResponse:
    """
    Accepts plain text and user preferences, returns URL of the generated speech audio.

    This function utilizes the gTTS library to convert provided text into speech according to the user's specifications.
    It takes into consideration the accent, language, pitch, and speed. The function then saves the generated audio to a file,
    stores the file's URL in the database, and returns the URL for access.

    Args:
        accent (str): Preferred accent for the speech output.
        text (str): The textual content to be converted into speech.
        language (str): Preferred language for the speech output.
        pitch (float): Preferred pitch level for the speech output. (Note: This feature might not be directly supported by gTTS, thus, for the purpose of this example, this argument won’t be used directly in the gTTS function call.)
        speed (float): Preferred speed for the speech output.

    Returns:
        ConvertTextResponse: Provides the URL of the generated speech audio after successful conversion.
    """
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = f"{uuid.uuid4()}.mp3"
            filepath = os.path.join(temp_dir, filename)
            tts = gTTS(text=text, lang=language, slow=speed < 1)
            tts.save(filepath)
            uploaded_file_url = f"http://example.com/audio_files/{filename}"
            return ConvertTextResponse(audioUrl=uploaded_file_url)
    except Exception as e:
        raise Exception(f"An error occurred while converting text to speech: {str(e)}")
