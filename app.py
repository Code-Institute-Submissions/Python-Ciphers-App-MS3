import os
from flask import Flask, render_template
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

USER_DATA = mongo.db.users.find_one({'email': "test1@test1.com"})
print(USER_DATA)

@app.route('/')
def index():
    return render_template('index.html')




# Prior to deployment set debug=False

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)