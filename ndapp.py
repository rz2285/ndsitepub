from flask import Flask, render_template, request, flash, url_for, abort, send_from_directory
import os
from datetime import datetime


app = Flask(__name__, static_url_path='')

app.config.from_pyfile('ndapp.cfg')

#error message
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found."

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

#service page
@app.route("/service")
def home():
	return render_template("service.html")


#contact page
@app.route("/contact")
def contact():
	return render_template("contact.html")

#our story page
@app.route("/ourstory")
def ourstory():
    return render_template("ourstory.html")


#community page
@app.route("/community")
def community():
    return render_template("community.html")

#privacy policy page
@app.route("/privacypolicy")
def privacy():
    return render_template("privacy.html")


#about page
@app.route("/about")
def about():
    return render_template("about.html")


#home page
@app.route("/")
def homegrid():
    return render_template("homegrid.html")

#trying to improve home page
@app.route("/2")
def homegrid2():
    return render_template("homegrid2.html")



#attempt at sign in page
@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/start_reservation")
def start_reservation():
    return render_template("start_reservation.html")

@app.route("/restaurant_categories")
def restaurant_categories():
    return render_template("restaurant_categories.html")

@app.route("/account_management")
def account_management():
    return render_template("account_management.html")

@app.route("/upcoming_reservation")
def upcoming_reservation():
    return render_template("upcoming_reservation.html")

@app.route("/give_feedback")
def give_feedback():
    return render_template("give_feedback.html")

@app.route("/reservation_history")
def reservation_history():
    return render_template("reservation_history.html")










if __name__ == "__main__":
	app.run()
