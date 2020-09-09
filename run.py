import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)  # initialise new flask app
app.secret_key = "random1234"
messages = []   # empty list to which username:messages will be appended


def add_messages(username, message):
    """add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(messages_dict)


@app.route('/', methods=["GET", "POST"])  # app root decorator for index page
def index():
    """Main page with instructions"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")


@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "<h1>Welcome, {0}</h1> {1}".format(username, messages)


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
