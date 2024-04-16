---
date: 2024-04-16T16:45:38.380876
author: AutoGPT <info@agpt.co>
---

# Text-to-Speech API

To fulfill the user's need for a text-to-speech conversion service, we will build an endpoint using the specified tech stack, which includes Python, FastAPI, PostgreSQL, and Prisma. The primary feature of this endpoint will be to accept plain text as input and convert it into natural-sounding speech audio. Based on the user's preferences and the search for the best Python package for text-to-speech conversion, we will utilize the gTTS (Google Text-to-Speech) library. This library is well-regarded for its ability to convert text into natural-sounding speech using Google's text-to-speech API. It supports multiple languages and accents, which aligns well with the user's requirement to cater to a global audience. Additionally, the gTTS library offers functionality that can be leveraged to tune the voice's pitch and speed, enhancing clarity and achieving a more natural sound, as requested. The generated speech audio will then be returned as an audio file to the endpoint caller. This solution aims to provide an efficient and user-friendly audio conversion service that meets the specified needs for voice customization and international support.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'Text-to-Speech API'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
