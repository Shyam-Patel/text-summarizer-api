from flask import Flask
from flask_cors import CORS
from Resources.APITest import APITest_Blueprint


def setup(_app):
    CORS(_app)  # Allows cross-origin API requests
    app.register_blueprint(APITest_Blueprint, url_prefix="/apitest")


app = Flask(__name__)
setup(app)
app.run()
