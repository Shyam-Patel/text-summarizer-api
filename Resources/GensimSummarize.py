from flask import Blueprint
from flask import jsonify
from flask import request
from gensim.summarization.summarizer import summarize
import Validation

GensimSummarize_Blueprint = Blueprint('gensim-module', __name__)


@GensimSummarize_Blueprint.route("/text", methods=['POST'])
def summarize():
    if not request.is_json:
        return jsonify("Invalid request")

    content = request.get_json()
    if not Validation.validate_request(content):
        return jsonify("Request does not match defined schema")

    return jsonify("Welcome, " + content['user'])
    #return jsonify("Here is your summary, " + content['user'] + ":\n" + summarize(content['text']))
