import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()
SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

def get_hotels(location, budget):
    query = f"cheap hotels in {location} under {budget} INR"
    params = {
        "engine": "google",
        "q": query,
        "location": "India",
        "api_key": SERP_API_KEY,
        "num": 5
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("organic_results", [])
