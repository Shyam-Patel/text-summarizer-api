from flask import Flask
from flask_cors import CORS
from Blueprints.GensimSummarize import GensimSummarize_Blueprint
from Blueprints.SumySummarize import SumySummarize_Blueprint


def setup(_app):
    # Enables cross-origin API requests
    CORS(_app)

    # Register all the blueprints (API endpoints)
    app.register_blueprint(GensimSummarize_Blueprint, url_prefix="/gensim")
    app.register_blueprint(SumySummarize_Blueprint, url_prefix="/sumy")


if __name__ == '__main__':
    app = Flask(__name__)
    setup(app)
    app.run()
