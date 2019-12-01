from flask import Blueprint
from flask import request
from Helpers import APIHelper as API
from Helpers import Validation
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

LuhnSummarizer_Blueprint = Blueprint('luhn-module', __name__)


@LuhnSummarizer_Blueprint.route("/text", methods=['POST'])
def text_summarize():
    if not Validation.validate_api_request(request=request, required_properties=["text", "ratio"]):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    json_content = request.get_json()

    parser = PlaintextParser.from_string(string=json_content['text'], tokenizer=Tokenizer('english'))
    summary = luhn_summarize(parser=parser, content=json_content['text'], ratio=json_content['ratio'])

    return API.api_response(response_code=API.success_code, message=summary)


@LuhnSummarizer_Blueprint.route("/url", methods=['POST'])
def url_summarize():
    if not Validation.validate_api_request(request=request, required_properties=["url", "ratio"]):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    json_content = request.get_json()

    parser = HtmlParser.from_url(url=json_content['url'], tokenizer=Tokenizer('english'))
    text_from_url = ' '.join(str(sentence) for sentence in parser.document.sentences)
    summary = luhn_summarize(parser=parser, content=text_from_url, ratio=json_content['ratio'])

    return API.api_response(API.success_code, summary)


def luhn_summarize(parser, content, ratio):
    luhn_summarizer = LuhnSummarizer()

    sentence_count = content.count('.')
    desired_sentence_count = round(sentence_count * ratio)

    summary_tuple_list = luhn_summarizer(parser.document, desired_sentence_count)
    summary = ' '.join(str(sentence) for sentence in summary_tuple_list)

    return summary
