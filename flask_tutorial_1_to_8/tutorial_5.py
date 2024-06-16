# sessions

from flask import Flask, redirect, render_template, url_for, request, session
from datetime import timedelta

app = Flask(__name__)

# secret ket required to use session, to encrypt and decrypt these data
app.secret_key = "hello"  

# this way we can store our session data for 5 days 
# we can also make it for minutes=5 to store session for 5 minutes
app.permanent_session_lifetime = timedelta(days=5)  


@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True        # set to true
        user = request.form["name"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        # if user is already logged in login page wont open it will redirect to user page
        if "user" in session:   
            return redirect(url_for("user"))
            
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session: 
        user = session["user"]
        return f"<h1>hello {user}</h1>"
    else:
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)