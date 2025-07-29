from gemini_api import generate_itinerary
from hotel_search import get_hotels

def plan_trip(destination, duration, budget, num_people, start_date):
    hotels = get_hotels(destination, budget)
    itinerary = generate_itinerary(destination, duration, budget, num_people, start_date)

    final_summary = f"""
### 📍 Location: {destination}
### 🕒 Duration: {duration} days
### 👥 People: {num_people}
### 💰 Budget: ₹{budget}
### 📅 Start Date: {start_date}

---

#### 🏨 Top Hotels Found:
"""
    for h in hotels[:3]:
        final_summary += f"- [{h['title']}]({h['link']})\n"

    final_summary += f"""
---

#### 📝 Suggested Itinerary:
{itinerary}
    """
    return final_summary