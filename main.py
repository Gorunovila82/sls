from flask import Flask

app = Flask(__name__)

@app.route("/")
def i2n():
    return "Hello world!"

app.run(port=80,host="0.0.0.0")
