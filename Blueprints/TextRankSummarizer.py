from flask import Blueprint
from flask import request
from Helpers import APIHelper as API
from Helpers import Validation
import gensim
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer


TextRank_Blueprint = Blueprint('textrank-module', __name__)


@TextRank_Blueprint.route("/text", methods=['POST'])
def text_summarize():
    if not Validation.validate_api_request(request=request, required_properties=["text", "ratio"]):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    json_content = request.get_json()

    summary = gensim.summarization.summarize(text=json_content['text'], ratio=json_content['ratio'])

    return API.api_response(API.success_code, summary)


@TextRank_Blueprint.route("/url", methods=['POST'])
def url_summarize():
    if not Validation.validate_api_request(request=request, required_properties=["url", "ratio"]):
        return API.api_response(API.failure_code, "Request does not match defined schema. Check documentation")

    json_content = request.get_json()

    parser = HtmlParser.from_url(url=json_content['url'], tokenizer=Tokenizer('english'))
    text_from_url = ' '.join(str(sentence) for sentence in parser.document.sentences)
    summary = gensim.summarization.summarize(text=text_from_url, ratio=json_content['ratio'])

    return API.api_response(API.success_code, summary)
