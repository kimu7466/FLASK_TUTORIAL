# HTTP methods (GET/POST) and retrieving form data

from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

@app.route("/login", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["name"]
        print(user)
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"hello {usr}"


if __name__ == "__main__":
    app.run(debug=True)