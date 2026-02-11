from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.ai_services import generate_itinerary

app = Flask(__name__)

# Budget mapping
BUDGET_MAP = {
    "Low Budget": 1000,
    "Medium Budget": 5000,
    "High Budget": 10000
}

# 1️⃣ Welcome page
@app.route("/", methods=["GET"])
def welcome():
    return render_template("welcome.html")


# 2️⃣ Places page
@app.route("/places", methods=["GET", "POST"])
def places():
    if request.method == "POST":
        # If you want to save any info from places.html, you can handle here
        return redirect(url_for('planner'))
    return render_template("places.html")
@app.route('/previous-trips')
def previous_trips():
    return render_template('previous_trips.html')



# 3️⃣ Planner page (current index.html)
@app.route("/planner", methods=["GET", "POST"])
def planner():
    if request.method == "POST":
        # Get basic fields
        destination = request.form.get("destination", "").strip()
        start_date_str = request.form.get("start_date", "2026-02-11")
        end_date_str = request.form.get("end_date", "2026-02-12")
        travelers = request.form.get("travelers", "1")

        # Convert dates and calculate days
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            days = (end_date - start_date).days + 1
            if days < 1:
                days = 1
        except ValueError:
            start_date = datetime(2026, 2, 11)
            end_date = datetime(2026, 2, 12)
            days = 1

        # Budget
        budget_text = request.form.get("budget", "Low Budget")
        budget = BUDGET_MAP.get(budget_text, 1000)

        # Interests (checkboxes)
        interests_list = request.form.getlist("interests")
        if not interests_list:
            interests_list = ["sightseeing"]

        # Transport (checkboxes)
        transport_list = request.form.getlist("transport")
        transport = ", ".join(transport_list) if transport_list else "Public Transport"

        # Generate itinerary
        itinerary = generate_itinerary(destination, days, budget, interests_list)

        # Render result page after planner submission
        return render_template(
            "result.html",
            destination=destination,
            days=days,
            budget=budget,
            interests=", ".join(interests_list),
            travelers=travelers,
            transport=transport,
            start_date=start_date_str,
            end_date=end_date_str,
            itinerary=itinerary
        )

    # GET request shows the planner form
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
