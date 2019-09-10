from flask import Blueprint
from flask import jsonify
from flask import request
from gensim.summarization.summarizer import summarize
import Validation

GensimSummarize_Blueprint = Blueprint('gensim-module', __name__)


@GensimSummarize_Blueprint.route("/text")
def summarize():
    if(request.is_json != True):
        return jsonify("Invalid request")

    content = request.get_json()
    Validation.validate_request(content)

    return jsonify("Here is your summary, " + content['user'] + ":\n" + summarize(content['text']))
