import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-pro")

def generate_itinerary(location, duration, budget, people, start_date):
    prompt = f"""
Create a travel itinerary for a group of {people} people visiting {location} for {duration} days starting on {start_date} with a total budget of ₹{budget}.
Include affordable activities, local travel, and must-visit places.
Format as markdown.
"""
    res = model.generate_content(prompt)
    return res.text