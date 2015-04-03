from flask import Flask, render_template, jsonify, request, flash, redirect
import requests
import json
from flaskext.mysql import MySQL



app = Flask(__name__, static_url_path='')

#do not inculed in finished app
app.config["DEBUG"] = True

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'devuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'devpwd'
app.config['MYSQL_DATABASE_DB'] = 'neurod_database'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


#error message
@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found."



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

    
    

#SEARCH A PHP FILE FROM SERVICES FOLDER
@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
        url = "http://localhost/neurodining/services/" + request.form["user_search"]
        response_dict = requests.get(url).json()
        return jsonify(response_dict)
    else: # request.method == "GET"
        return render_template("search.html")

#initial attempts to create login page
@app.route("/a", methods=["POST", "GET"])
def a():
    if  request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from TABLE_CUSTOMERS where Username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        url = "http://localhost/neurodining/services/sign_up.php"
        return requests.get(url).json()
 #       if data is None:
  #          return "Username or Password is wrong"
   #     else:
    #        return "Logged in successfully"
    else:
        return render_template("search.html")

#Following flask mysql tutorial http://www.techillumination.in/2014/01/python-web-application-development.html 
@app.route("/Authenticate", methods=["POST", "GET"])
def Authenticate():
    if request.method == "POST":
        customer = request.form["customers_firstname"]
        password = request.form["pass_raw"]
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from customers where customers_firstname='" + customer + "' and pass_raw='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            return "This customer is not on the list."
        else:
            return "This customer is on the list."
    else: 
        return render_template("signin.html")

#customer = request.args.get('customers_firstname')
    #password = request.args.get('pass_raw')







if __name__ == "__main__":
	app.run(host="0.0.0.0")
