# static files

from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)


