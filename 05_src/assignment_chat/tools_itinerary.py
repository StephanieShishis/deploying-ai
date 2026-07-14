from langchain.tools import tool
from typing import Optional
 
DAY_IDEAS = {
    "culture": "Visit a UNESCO World Heritage Site or a local museum.",
    "food": "Try a food market or a well-reviewed local restaurant.",
    "nature": "Spend the day on a hike or at a scenic viewpoint.",
    "relaxation": "Slow down with a spa, a park, or a long coffee break.",
    "adventure": "Book an excursion like biking or rafting.",
}
 
DEFAULT_INTERESTS = ["culture", "food", "nature"]
 
@tool
def build_itinerary(city: str, days: int, interests: Optional[list[str]] = None) -> str:
    """
    This builds a simple itinerary for a trip. `interests` should be chosen from: culture, food, nature, relaxation, adventure. 
    If not given, a default mix is used.
    """
    days = max(1, min(days, 14))
 
    chosen = []
    if interests:
        for interest in interests:
            if interest.lower() in DAY_IDEAS:
                chosen.append(interest.lower())
    if not chosen:
        chosen = DEFAULT_INTERESTS
 
    lines = [f"{days}-day itinerary for {city}:"]
    for day in range(1, days + 1):
        interest = chosen[(day - 1) % len(chosen)]
        lines.append(f"Day {day} ({interest}): {DAY_IDEAS[interest]}")
 
    return "\n".join(lines)
 
