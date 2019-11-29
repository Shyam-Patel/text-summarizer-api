from flask import Blueprint
from flask import request
from Helpers import APIHelper as API
from Helpers import Validation

LuhnSummarizer_Blueprint = Blueprint('luhn-module', __name__)


@LuhnSummarizer_Blueprint.route("/text", methods=['POST'])
def summarize():
    if not Validation.validate_api_request(request, ["text"]):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    json_content = request.get_json()

    return API.api_response(API.success_code, "Feature not available yet.")
