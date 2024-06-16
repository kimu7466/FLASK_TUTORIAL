# Blueprints & using multiple python file

from flask import Flask, render_template
from admin.second_file import second_app


app = Flask(__name__)
app.register_blueprint(second_app,url_prefix="/admin")

@app.route("/")
def test():
    return "<h1>TEST</h1>"


if __name__ == "__main__":
    app.run(debug=True)