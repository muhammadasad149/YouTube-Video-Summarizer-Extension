from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()  # Load all the environment variables

app = FastAPI()

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class YouTubeLink(BaseModel):
    link: str

@app.post("/get_detailed_notes/")
async def get_detailed_notes(link: YouTubeLink):
    def extract_transcript_details(youtube_video_url):
        try:
            video_id = youtube_video_url.split("=")[1]
            transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

            transcript = ""
            for i in transcript_text:
                transcript += " " + i["text"]

            return transcript

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def generate_gemini_content(transcript_text, prompt, length):
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt.format(length=length) + transcript_text)
        return response.text

    transcript_text = extract_transcript_details(link.link)

    if transcript_text:
        prompt = """You are Yotube video summarizer. You will be taking the transcript text
        and summarizing the entire video and providing the important summary in points
        within {length} words. Please provide the summary of the text given here:  """
        summary = generate_gemini_content(transcript_text, prompt, length=250)
        return {"detailed_notes": summary}
    else:
        raise HTTPException(status_code=404, detail="Transcript not found")

# Handle OPTIONS requests for the /get_detailed_notes/ endpoint
@app.options("/get_detailed_notes/")
async def options_detailed_notes():
    return {"Allow": "POST"}  # Specify allowed methods for CORS preflight requests


