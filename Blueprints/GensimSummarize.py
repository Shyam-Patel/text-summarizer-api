from flask import Blueprint
from flask import request
from Helpers import APIHelper as API
from Helpers import Validation
import gensim

GensimSummarize_Blueprint = Blueprint('gensim-module', __name__)


@GensimSummarize_Blueprint.route("/text", methods=['POST'])
def summarize():
    json_content = API.fetch_request_json(request)

    if json_content is None:
        return API.api_response(API.failure_code, "Request is not in JSON format")

    if not Validation.summary_request(json=json_content, must_have_property='text'):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    if json_content['ratio']:
        summary = gensim.summarization.summarize(json_content['text'], json_content['ratio'])
    else:
        summary = gensim.summarization.summarize(json_content['text'])

    return API.api_response(API.success_code, summary)
