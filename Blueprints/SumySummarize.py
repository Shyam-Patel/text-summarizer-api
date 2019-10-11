from flask import Blueprint
from flask import request
from Helpers import APIHelper as API
from Helpers import Validation

SumySummarize_Blueprint = Blueprint('sumy-module', __name__)

@SumySummarize_Blueprint.route("/text", methods=['POST'])
def summarize():
    if not Validation.validate_api_text_request(request, ["text"]):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    json_content = request.get_json()

    return None
