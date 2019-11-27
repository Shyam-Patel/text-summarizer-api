from flask import Flask
from flask_cors import CORS
from Blueprints.GensimSummarize import GensimSummarize_Blueprint
from Blueprints.SumySummarize import SumySummarize_Blueprint
from Helpers import APIHelper as API

app = Flask("TS-API")


@app.route('/')
def index():
    # Enables cross-origin API requests
    CORS(app)

    # Register all the blueprints (API endpoints)
    app.register_blueprint(GensimSummarize_Blueprint, url_prefix="/gensim")
    app.register_blueprint(SumySummarize_Blueprint, url_prefix="/sumy")

    return API.api_response(API.success_code, "Welcome to the Text Summarizer API!")