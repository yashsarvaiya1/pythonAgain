from flask import Flask
from flask import render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def hello_yash():
    return "Hello Yash"

@app.route("/<name>")
def hello_there(name):
    return "hello," + name

if __name__ == "__main__":
    app.run(debug=True)
