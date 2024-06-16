# flask making app and running server

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "hello! imroz this is the main Page.<a href='www.google.com'>hiiii</a><br><h1>IRMOZ KHAN</h1>"

@app.route("/<name>")
def user(name):
    return f"hello! {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()