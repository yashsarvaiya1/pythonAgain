from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_yash():
    return "Hello Yash"

@app.route("/<name>")
def hello_there(name):
    return "hello," + name

@app.route("/html",methods=["GET"])
def html():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

