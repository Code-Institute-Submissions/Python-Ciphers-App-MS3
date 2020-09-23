import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)

""" 
MONGO_URI was set locally for my localhost app development and testing.
vim ~/.bashrc
export MONGO_URI="MONGO_URL"
:wr save and exit then enter command
source ~/.bashrc
"""

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = "ms3_trial"

mongo = PyMongo(app)


@app.route('/')
def index():
    """
    This function renders the home page content when the user visits "/" and is logged in, otherwise it renders the registration page
    Once a user is authenticated there's no need to authenticate him again 
    """
    username = session.get('username')
    if username:
        users = mongo.db.users.find()
        return render_template('index.html', users=users)
    return render_template('register.html')




# Prior to deployment set debug=False

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)