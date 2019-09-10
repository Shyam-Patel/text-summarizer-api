from flask import Flask
from flask_cors import CORS
from Resources.APITest import APITest_Blueprint
from Resources.GensimSummarize import GensimSummarize_Blueprint


def setup(_app):
    CORS(_app)  # Allows cross-origin API requests
    app.register_blueprint(APITest_Blueprint, url_prefix="/apitest")
    app.register_blueprint(GensimSummarize_Blueprint, url_prefix="/summarize")


if __name__ == '__main__':
    app = Flask(__name__)
    setup(app)
    app.run()
