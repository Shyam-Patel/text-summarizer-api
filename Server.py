from flask import Flask
from flask_cors import CORS
from Blueprints.GensimSummarize import GensimSummarize_Blueprint
from Blueprints.SumySummarize import SumySummarize_Blueprint

app = Flask(__name__)


@app.route("/")
def setup():
    # Enables cross-origin API requests
    CORS(app)

    # Register all the blueprints (API endpoints)
    app.register_blueprint(GensimSummarize_Blueprint, url_prefix="/gensim")
    app.register_blueprint(SumySummarize_Blueprint, url_prefix="/sumy")

    app.run()
