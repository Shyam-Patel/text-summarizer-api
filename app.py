from flask import Flask
from flask_cors import CORS
from Blueprints.TextRankSummarizer import TextRank_Blueprint
from Blueprints.LuhnSummarizer import LuhnSummarizer_Blueprint
from Helpers import APIHelper as API

app = Flask("TS-API")

# Enables cross-origin API requests
CORS(app)

# Register all the blueprints (API endpoints)
app.register_blueprint(TextRank_Blueprint, url_prefix="/textrank")
app.register_blueprint(LuhnSummarizer_Blueprint, url_prefix="/luhn")

if __debug__:
    app.run() #this statement should not run when deployed since it will host the Flask API at a differing URL then what 'gunicorn' uses


@app.route('/')
def index():
    return API.api_response(API.success_code, "Welcome to the Text Summarizer API!")
