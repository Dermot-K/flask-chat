import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)  # initialise new flask app
app.secret_key = "random1234"
messages = []   # empty list to which username:messages will be appended


def add_message(username, message):
    """add messages to the 'messages' list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})


@app.route('/', methods=["GET", "POST"])  # app root decorator for index page
def index():
    """Main page with instructions"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")


@app.route('/chat/<username>', methods=["GET", "POST"])
def user(username):
    """add and display chat messages"""

    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))

    return render_template("chat.html", username=username,
                           chat_messages=messages)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
