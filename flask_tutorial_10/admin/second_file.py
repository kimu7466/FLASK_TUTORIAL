from flask import Blueprint, render_template

second_app = Blueprint("second_file", __name__, static_folder="static", template_folder="templates")


@second_app.route("/home")
@second_app.route("/")
def home():
    return render_template("home.html")

