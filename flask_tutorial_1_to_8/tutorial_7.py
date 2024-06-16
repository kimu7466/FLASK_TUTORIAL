# using SQLAlchemy database

# install command :- pip install flask-sqlalchemy

# message flashing

from flask import Flask, redirect, render_template , session, url_for, request, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy # firstly import 

app = Flask(__name__)

app.secret_key = "hello"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONs"] = False

app.permanent_session_lifetime = timedelta(hours=1) 

db = SQLAlchemy(app)  # create a database object

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.colum(db.String(100))
    email = db.colum(db.String(100))

    def __init__(self, name , email):
        self.name = name
        self.email = email

@app.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        flash("login successfully.", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("already logged in.", "info")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user", methods =  ["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method =="POST":
            email = request.form["email"]
            session["email"] = email
        else:
            if "email" in session:
                email = session["email"]
                
        return render_template("8_user_form.html", email=email)
    else:
        flash("you are not logged in.")
        return redirect("login")


@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"] 
        flash(f"{user} you have been logged out!", "info")
    session.pop("user", None)
    return redirect("login")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

