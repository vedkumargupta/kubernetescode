from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to our new code deployed by the Team!!!'
