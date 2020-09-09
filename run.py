import os
from flask import Flask

app = Flask(__name__)  # initialise new flask app


@app.route('/')  # app root decorator for index page
def index():
    return "<h1>Hello</h1>"


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
