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


@app.route('/register', methods=['POST', 'GET'])
def register():
    """
    This function handles user registration:
    If the user tries to register with a username or a previously registered email that already exists in DB we notify
    Otherwise we crate the user entry data dictionary and insert it into DB
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = {'username': username, 'email': email, 'password': password}

        if mongo.db.users.find_one({"username": username}): 
            return 'This User already exists'
        elif mongo.db.users.find_one({"email": email}):
            return 'This Email was already used for registration'
        else:
            mongo.db.users.insert_one(user)
            session['username'] = user['username']
            return render_template('index.html', email=user['email'], password=user['password'])

    return render_template('register.html')



# Prior to deployment set debug=False

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)