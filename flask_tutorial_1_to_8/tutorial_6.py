# message flashing

from flask import Flask, redirect, render_template , session, url_for, request, flash
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(hours=1) 

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

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
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
    app.run(debug=True)

