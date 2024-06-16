# templates and contexts 

from flask import Flask, render_template

app = Flask(__name__)

""" template folder must be in the same directory as the main app file is. """


# @app.route("/")
# def home():
#     return render_template("index.html")



# we need to put name as endpoint like this http://127.0.0.1:5000/test123
@app.route("/<name>")  
def home(name):
    name_list = ["imroz", "aadil", "basid", "yasin"]
    return render_template("index.html", content = name, number = 12345, users = name_list)


if __name__ == "__main__":
    app.run()