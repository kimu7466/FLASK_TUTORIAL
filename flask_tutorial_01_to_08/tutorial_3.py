# template inheritance and debug mode

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("toturial_3.html")


@app.route("/test")
def new():
    return render_template("new.html")


if __name__ == "__main__":
    app.run(debug=True)               # debug=True /keyword/ this will allow us to not rerun the server every time we make changes
