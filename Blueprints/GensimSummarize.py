from flask import Blueprint
from flask import request
from Helpers import APIHelper as API
from Helpers import Validation
import gensim

GensimSummarize_Blueprint = Blueprint('gensim-module', __name__)


@GensimSummarize_Blueprint.route("/text", methods=['POST'])
def summarize():
    if not Validation.validate_api_text_request(request, ['text']):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    json_content = request.get_json()

    if json_content['ratio']:
        summary = gensim.summarization.summarize(json_content['text'], json_content['ratio'])
    else:
        summary = gensim.summarization.summarize(json_content['text'])

    return API.api_response(API.success_code, summary)
