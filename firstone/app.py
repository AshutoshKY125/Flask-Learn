from flask import Flask


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello its working"

@app.route("/index")
def index():
    return ("this is index page")



if __name__ == "__main__":
    app.run(debug = True)