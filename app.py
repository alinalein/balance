import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def home():
    #we chech the session for the user
    user_id = session["user_id"]
    #select the ids of the calorie values
    ids = db.execute("SELECT id FROM details WHERE user_id =?", user_id)
    # set default values for when the user has not calculated his recommended calorie intake jet.
    if len(ids) == 0:
        return render_template("home.html",cal="Empty", total_cal="Empty", bmr="Empty", allowed="Empty")
    #select the calorie amount the user consumed today
    date = datetime.date.today()
    calories = db.execute("SELECT SUM(calories) AS calories FROM calories WHERE date=? AND user_id =? ", date, user_id)
    #select the recommended calorie intake for the user
    total_cal = db.execute("SELECT total_cal FROM details WHERE user_id=?",user_id)
    #select the bmr calorie intake for the user
    bmr = db.execute("SELECT bmr FROM details WHERE user_id=?",user_id)
    #calculate the calorie amount the user should consume for the day
    allowed = total_cal[0]["total_cal"]
    cal = calories[0]["calories"]

    if len(total_cal) !=0 and calories[0]["calories"] != None:
        tmp = total_cal[0]["total_cal"] - cal
        allowed = str(tmp)
    #send the values to the html file
    return render_template("home.html",cal=cal, total_cal=total_cal[0]["total_cal"], bmr=bmr[0]["bmr"], allowed=allowed)

@app.route("/login", methods=["GET", "POST"])
def login():
    # Log user in

    # Forget any user_id
    session.clear()

    # User reached route via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM user WHERE username = ?", request.form.get("username"))

        # Check if username exists or password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # GET request
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/calories", methods=["GET", "POST"])
@login_required
def calories():
    #Count calories and display them
    if request.method == "POST":
        user_id = session["user_id"]
        calories = str(request.form.get("calories"))
        food = request.form.get("food")
        date = datetime.date.today()
        if not calories or not food:
            return apology("Please fill in all fields")
        if int(calories) <= 0:
            return apology("Calories can`t be negative")

        db.execute("INSERT INTO calories (user_id, calories, food, date) VALUES(?,?,?,?)", user_id, calories, food, date)
        return redirect("/calories")
    else:
        user_id = session["user_id"]
        calories_db = db.execute("SELECT * FROM calories WHERE user_id=? ORDER BY date DESC", user_id)
    return render_template("calories.html", calories=calories_db)

@app.route("/delete", methods=["POST"])
@login_required
def delete():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM calories WHERE id = ?", id)
    return redirect("/calories")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    else:
        # Get username, password, confirmation from HTML
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # If one of the values will miss , send to apology.html
        if not username:
            return apology("Username is missing")

        if not password:
            return apology("Password is missing")

        if not confirmation:
            return apology("Confirmation is missing")
        # Make sure the password and the confirmation are the same
        if password != confirmation:
            return apology("Confirmation password does not match the password")

        # Generete hash password
        hash = generate_password_hash(password)

        # Add new user to database + give it the value new_user
        try:
            new_user = db.execute("INSERT INTO user (username, hash) VALUES (?, ?)", username, hash)

        # If username already exists, send to apology.html
        except:
            return apology("username already exists")

        # Remeber user, so user has not to login again and send to index page
        session["user_id"] = new_user
        return redirect("/")

@app.route("/start", methods=["GET", "POST"])
@login_required
def start():
    if request.method == "GET":
        return render_template("start.html")
    else:
        age = str(request.form.get("age"))
        height = str(request.form.get("height"))
        weight = str(request.form.get("weight"))

        activity = request.form.get("activity")
        gender = request.form.get("gender")
        user_id = session["user_id"]

        if not age:
            return apology("Please fill in all fields")
        if not height or not weight or not activity or not gender:
            return apology("Please fill in all fields")
        if int(age) <= 0 or int(height) <= 0 or int(weight) <= 0:
            return apology("All values have to be positive")

        if gender == "female":
            bmr = round((9.6 * int(weight)) + (1.8 * int(height)) - (4.7 * int(age)) + 655)
        else:
            bmr = round((13.7 * int(weight)) + (5.0 * int(height)) - (6.8 * int(age)) + 66)

        if activity =="sedentary":
            total_cal = round(bmr * 1.2)
        elif activity =="light":
            total_cal = round(bmr * 1.375)
        elif activity =="moderate":
            total_cal = round(bmr * 1.55)
        else:
            total_cal = round(bmr * 1.725)

        ids = db.execute("SELECT id FROM details WHERE user_id =?", user_id)
        if len(ids) == 0:
            db.execute("INSERT INTO details (age, height, weight, activity, gender, user_id, bmr, total_cal) VALUES(?,?,?,?,?,?,?,?)", age, height, weight, activity, gender, user_id, bmr, total_cal)
        else:
            db.execute("UPDATE details SET age = ?, height =?, weight=?, activity=?, gender=?, bmr=?, total_cal=? WHERE user_id=?", age, height, weight, activity, gender, bmr, total_cal, user_id)

        return redirect("/")