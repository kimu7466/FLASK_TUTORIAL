from flask import Flask, redirect, render_template, session, url_for, request, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "hello"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.permanent_session_lifetime = timedelta(hours=1)

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user

        found_user = Users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = Users(user, "")
            db.session.add(usr)
            db.session.commit()
            found_user = usr 
            
        flash("Login successful.", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in.", "info")
            return redirect(url_for("user"))
        
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = Users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email saved.")
        else:
            if "email" in session:
                email = session["email"]
                
        return render_template("8_user_form.html", email=email)
    else:
        flash("You are not logged in.")
        return redirect(url_for("login"))

@app.route("/view")
def view():
    return render_template("view.html", values=Users.query.all())

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"{user}, you have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/delete")
def delete():
    if "user" in session:
        user = session["user"]
        usr = Users.query.filter_by(name=user).first()

        if usr:
            db.session.delete(usr)
            db.session.commit()
            session.pop("user", None)
            session.pop("email", None)
            flash("Account deleted successfully.")
        else:
            flash("User not found.")
    else:
        flash("You are not logged in.")
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
