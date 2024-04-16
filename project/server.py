import logging
from contextlib import asynccontextmanager

import project.convert_text_to_speech_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="Text-to-Speech API",
    lifespan=lifespan,
    description="To fulfill the user's need for a text-to-speech conversion service, we will build an endpoint using the specified tech stack, which includes Python, FastAPI, PostgreSQL, and Prisma. The primary feature of this endpoint will be to accept plain text as input and convert it into natural-sounding speech audio. Based on the user's preferences and the search for the best Python package for text-to-speech conversion, we will utilize the gTTS (Google Text-to-Speech) library. This library is well-regarded for its ability to convert text into natural-sounding speech using Google's text-to-speech API. It supports multiple languages and accents, which aligns well with the user's requirement to cater to a global audience. Additionally, the gTTS library offers functionality that can be leveraged to tune the voice's pitch and speed, enhancing clarity and achieving a more natural sound, as requested. The generated speech audio will then be returned as an audio file to the endpoint caller. This solution aims to provide an efficient and user-friendly audio conversion service that meets the specified needs for voice customization and international support.",
)


@app.post(
    "/convert",
    response_model=project.convert_text_to_speech_service.ConvertTextResponse,
)
async def api_post_convert_text_to_speech(
    accent: str, text: str, language: str, pitch: float, speed: float
) -> project.convert_text_to_speech_service.ConvertTextResponse | Response:
    """
    Accepts plain text and user preferences, returns URL of the generated speech audio.
    """
    try:
        res = await project.convert_text_to_speech_service.convert_text_to_speech(
            accent, text, language, pitch, speed
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
