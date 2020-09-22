import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h2>Hello Python-Ciphers-App</h2>"



# Prior to deployment set debug=False

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)