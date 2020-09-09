import os
from flask import Flask

app = Flask(__name__)  # initialise new flask app
messages = []   # empty list to which username:messages will be appended


def add_messages(username, message):
    messages.append("{}: {}".format(username, message))


@app.route('/')  # app root decorator for index page
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "Welcome, {0}".format(username, messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    return "{0}: {1}".format(username, message)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
