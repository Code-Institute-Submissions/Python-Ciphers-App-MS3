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
app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = "ms3_trial"

mongo = PyMongo(app)


@app.route('/')
def index():
    """
    This function renders the home page content when the user visits "/" and is logged in, otherwise it renders the registration page
    Once a user is authenticated there's no need to authenticate him again 
    As far as authentication goes the only part database use is mandatory is when you want to check the username and password, we do this in login function
    """
    username = session.get('username')
    if username:
        users = mongo.db.users.find()
        return render_template('index.html', users=users)
    return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    """
    This function handles user login as following:
    It renders home page if the user is logged in
    If the user is trying to login via POST/Submit method we grab from DB the USER_DATA by filtering using email address 
    and if the password introduced in the form matches the DB password then login is succesful
    If the user email does not match the user password in DB we return an error. We don't want a user to login with another user valid password but only his/her personal one.
    If the user tries to login with an email or password that does not exist in DB we intuitively render registration page
    """
    username = session.get('username')
    if username:
        users = mongo.db.users.find()
        return render_template('index.html', users=users)
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            USER_DATA = mongo.db.users.find_one({'email': email})
            if USER_DATA:
                if password == USER_DATA['password']:
                    session['username'] = USER_DATA['username']
                    print(session['username'])
                    return render_template('index.html')
                else:
                    return 'Invalid email or password'
            else:
                return render_template('register.html')
        return render_template('login.html')
 
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

@app.route('/logout')
def logout():
    """
    This function handles user logout
    The passing of the default None value prevents the KeyError exception being raised in case someone who is not logged in would access /logout 
    """
    session.pop('username', None)
    return redirect('/login')

@app.route('/intro_to_cryptography')
def intro_to_cryptography():
    # Renders the intro-to-cryptography page
    addCipher = mongo.db.ciphers.find()
    return render_template('intro-to-cryptography.html', addCipher=addCipher)

@app.route('/reverse_cipher')
def reverse_cipher():
    # Renders the reverse-cipher page
    return render_template('reverse-cipher.html')

@app.route('/caesar_cipher')
def caesar_cipher():
    # Renders the caesar-cipher page
    return render_template('caesar-cipher.html')

@app.route('/transposition_cipher')
def transposition_cipher():
    # Renders the transposition-cipher page
    return render_template('transposition-cipher.html')

@app.route('/affine_cipher')
def affine_cipher():
    # Renders the affine-cipher page
    return render_template('affine-cipher.html')

@app.route('/vigenere_cipher')
def vigenere_cipher():
    # Renders the vigenere-cipher page
    return render_template('vigenere-cipher.html')

@app.route('/your_ciphers')
def your_ciphers():
    # Renders your_ciphers page with the existent ciphers data from mongoDB
    addCipher = mongo.db.ciphers.find()
    return render_template('your-ciphers.html', add_cipher=addCipher)


# Prior to deployment set debug=False

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)