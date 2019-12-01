from flask import Blueprint
from flask import request
from Helpers import APIHelper as API
from Helpers import Validation
from Helpers import SumyHelper

LuhnSummarizer_Blueprint = Blueprint('luhn-module', __name__)


@LuhnSummarizer_Blueprint.route("/text", methods=['POST'])
def text_summarize():
    if not Validation.validate_api_request(request=request, required_properties=["text", "ratio"]):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    json_content = request.get_json()
    summary = SumyHelper.get_summary(summarizer_to_use="luhn", content=json_content["text"], content_type="text", ratio=json_content["ratio"])

    return API.api_response(response_code=API.success_code, message=summary)


@LuhnSummarizer_Blueprint.route("/url", methods=['POST'])
def url_summarize():
    if not Validation.validate_api_request(request=request, required_properties=["url", "ratio"]):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    json_content = request.get_json()
    summary = SumyHelper.get_summary(summarizer_to_use="luhn", content=json_content["url"], content_type="url", ratio=json_content["ratio"])

    return API.api_response(API.success_code, summary)

