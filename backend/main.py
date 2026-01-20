from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create FastAPI app
app = FastAPI(
    title="Gemini City Brain API",
    description="Backend API for Gemini City Brain Hackathon Project",
    version="1.0"
)

# Request model
class CityRequest(BaseModel):
    location: str
    proposal: str

# Root endpoint (health check)
@app.get("/")
def root():
    return {"status": "Gemini City Brain backend running 🚀"}

# Main Gemini-powered endpoint
@app.post("/analyze")
def analyze_city(data: CityRequest):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    You are an urban planning AI.

    Location: {data.location}
    Proposal: {data.proposal}

    Analyze the impact on:
    - Traffic
    - Pollution
    - Safety
    - Cost

    Give 3 alternative solutions and recommend the best one.
    """

    response = model.generate_content(prompt)

    return {
        "analysis": response.text
    }
