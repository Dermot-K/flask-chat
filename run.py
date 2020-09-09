import os
from datetime import datetime
from flask import Flask, redirect, render_template

app = Flask(__name__)  # initialise new flask app
messages = []   # empty list to which username:messages will be appended


def add_messages(username, message):
    """add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))


def get_all_messages():
    """get all of the messages and separate them with a 'br'"""
    return "<br>".join(messages)


@app.route('/')  # app root decorator for index page
def index():
    """Main page with instructions"""
    return render_template("index.html")


@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1> {1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
