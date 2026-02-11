# services/ai_services.py
import random

# Offline database of Indian cities
CITY_DATA = {
    "hampi": {
        "landmarks": [
            "Virupaksha Temple", "Vittala Temple Complex", "Hampi Bazaar",
            "Lotus Mahal", "Elephant Stables", "Matanga Hill", "Sasivekalu Ganesha",
            "Hazara Rama Temple"
        ],
        "restaurants": [
            "Mango Tree Restaurant", "Laughing Buddha Café", "Gopi Guest House Cafe",
            "Chillout Hampi"
        ]
    },
    "tirupati": {
        "landmarks": [
            "Tirumala Venkateswara Temple", "Sri Kapileswara Swamy Temple",
            "Talakona Waterfalls", "Sri Venkateswara Museum"
        ],
        "restaurants": [
            "Tirupati Mess", "Minerva Coffee Shop", "Sri Sai Grand Restaurant"
        ]
    },
    "bengaluru": {
        "landmarks": [
            "Bangalore Palace", "Lalbagh Botanical Garden", "Cubbon Park",
            "Vidhana Soudha", "Tipu Sultan's Summer Palace", "ISKCON Temple"
        ],
        "restaurants": [
            "MTR", "Vidyarthi Bhavan", "Karavalli", "Toit Brewery"
        ]
    },
    "hyderabad": {
        "landmarks": [
            "Charminar", "Golconda Fort", "Hussain Sagar Lake",
            "Ramoji Film City", "Salar Jung Museum", "Birla Mandir"
        ],
        "restaurants": [
            "Paradise Biryani", "Bawarchi", "Chutneys", "Olive Bistro"
        ]
    },
    "chennai": {
        "landmarks": [
            "Marina Beach", "Kapaleeshwarar Temple", "Fort St. George",
            "Santhome Cathedral", "Guindy National Park"
        ],
        "restaurants": [
            "Saravana Bhavan", "Murugan Idli Shop", "Southern Spice", "Bay View Restaurant"
        ]
    },
    "delhi": {
        "landmarks": [
            "Red Fort", "India Gate", "Qutub Minar",
            "Lotus Temple", "Humayun's Tomb", "Jama Masjid"
        ],
        "restaurants": [
            "Karim's", "Bukhara", "Rajinder Da Dhaba", "Saravana Bhavan"
        ]
    },
    "agra": {
        "landmarks": [
            "Taj Mahal", "Agra Fort", "Fatehpur Sikri",
            "Itimad-ud-Daulah", "Mehtab Bagh"
        ],
        "restaurants": [
            "Pinch of Spice", "Dasaprakash", "Joney’s Place", "Peshawri"
        ]
    },
    "jaipur": {
        "landmarks": [
            "Amber Fort", "City Palace", "Hawa Mahal",
            "Jantar Mantar", "Nahargarh Fort", "Jaipur Markets"
        ],
        "restaurants": [
            "LMB", "Chokhi Dhani", "Suvarna Mahal", "Spice Court"
        ]
    }
}

WEATHER_CONDITIONS = ["Sunny", "Cloudy", "Rainy", "Windy", "Partly Cloudy"]

def generate_itinerary(destination, days, budget, interests):
    """
    Generate a structured multi-day itinerary with landmarks, restaurants, and activities.
    """
    itinerary = []
    city_key = destination.lower()

    landmarks = CITY_DATA.get(city_key, {}).get("landmarks", [f"Famous place in {destination}"])
    restaurants = CITY_DATA.get(city_key, {}).get("restaurants", [f"Popular restaurant in {destination}"])

    # Loop over each day
    for day_num in range(1, days + 1):
        temp = random.randint(25, 38)
        condition = random.choice(WEATHER_CONDITIONS)
        weather_tip = "Good day for sightseeing!" if condition in ["Sunny", "Partly Cloudy"] else "Carry an umbrella and wear waterproof shoes."

        # Define time slots for the day
        time_slots = [
            "09:00", "09:30", "10:30", "12:00", "13:00", "14:30",
            "16:00", "17:30", "19:00", "20:30"
        ]

        day_plan = []
        for i, time in enumerate(time_slots):
            if i == 0:
                activity = f"Breakfast at {random.choice(restaurants)}"
            elif i in [1, 2, 3]:
                activity = f"Visit {random.choice(landmarks)}"
            elif i == 4:
                activity = f"Lunch at {random.choice(restaurants)}"
            elif i in [5, 6]:
                activity = f"{random.choice(interests).capitalize()} activity"
            elif i == 7:
                activity = f"Evening coffee/snack at {random.choice(restaurants)}"
            else:
                activity = f"Dinner at {random.choice(restaurants)}"

            day_plan.append({"time": time, "activity": activity})

        itinerary.append({
            "day": day_num,
            "plan": day_plan,
            "weather": {"temperature": temp, "condition": condition, "tip": weather_tip},
            "tips": "Carry water, wear comfortable shoes, check local timings."
        })

    estimated_cost_per_day = round(budget / days, 2)

    return {
        "destination": destination,
        "days": days,
        "budget": budget,
        "estimated_cost_per_day": estimated_cost_per_day,
        "itinerary": itinerary
    }
