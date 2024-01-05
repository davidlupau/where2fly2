import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///travel.db")

# Loading homepage
@app.route("/")
def index():
    return render_template("index.html")

# Loading page about weather
@app.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "GET":
        #Loading the list of countries from the database to be displayed in dropdown menu
        country_list = db.execute("SELECT country_name FROM countries ORDER BY country_name")
        return render_template("weather.html", country_list=country_list)

    else:
        # Get the information about temperatures, sunshine hours and sea temperature for the requested country
        country = request.form.get("country_list")
        temperatures = db.execute("SELECT * FROM temperatures WHERE country_name = ? ORDER BY city", country)
        sunshine = db.execute("SELECT * FROM sunshine WHERE country_name = ? ORDER BY city", country)
        sea = db.execute("SELECT * FROM sea WHERE country_name = ? ORDER BY city", country)

        # Return data to be displayed
        return render_template("weather_results.html", temperatures=temperatures, sunshine=sunshine, sea=sea, country=country)


# Loading page to get more info about selected country
@app.route("/countries", methods=["GET", "POST"])
def countries():
    if request.method == "GET":
        #Loading the list of countries from the database to be displayed in dropdown menu
        country_list = db.execute("SELECT country_name FROM countries ORDER BY country_name")
        return render_template("countries.html", country_list=country_list)

    else:
        # Get all the information about the requested country
        country = request.form.get("country_list")
        country_details = db.execute("SELECT * FROM countries WHERE country_name = ?", country)

        # Return data to be displayed
        return render_template("countries_results.html", country_details=country_details, country=country)


# Load page listing sources
@app.route("/sources", methods=["GET"])
def sources():
    if request.method == "GET":
        return render_template("sources.html")


# Load the page with search form
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")

    else:
        # Get the information from user
        region = request.form.get("region")
        period = request.form.get("when")
        type = request.form.get("type")
        flight = request.form.get("flight")

        # If user didn't provide all inputs
        if region == "null" or period == "null" or type == "null" or flight == "null":
            return render_template("error.html")

        else:
            countries = db.execute("SELECT country_name FROM type WHERE type = ? AND month = ? AND country_name IN (SELECT country_name FROM flights WHERE region = ? AND flight = ?) ORDER BY country_name", type, period, region, flight)

        # If search does not return any results
        if len(countries) == 0:
            return render_template("search_no_results.html")

        else:
            # Return data to be displayed
            return render_template("search_results.html", countries=countries)


# Load page about Cost of Living Index
@app.route("/cost_living", methods=["GET"])
def cost_living():
    if request.method == "GET":
        #Loading the indexes from the database
        cost_living = db.execute("SELECT * FROM cost_living ORDER BY cost_living_index DESC")
        return render_template("cost_living.html", cost_living=cost_living)