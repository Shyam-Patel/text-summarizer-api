from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.luhn import LuhnSummarizer
import nltk

LANGUAGE = "english"
nltk.download('punkt')

# These helper methods interfaces with the Sumy library to perform the various summarizations
def get_summary(summarizer_to_use, content, content_type, ratio):

    if content_type == "text":
        parser = PlaintextParser.from_string(string=content, tokenizer=Tokenizer(LANGUAGE))
        sentence_count = content.count('.')
    elif content_type == "url":
        parser = HtmlParser.from_url(url=content, tokenizer=Tokenizer(LANGUAGE))
        text_from_url = ' '.join(str(sentence) for sentence in parser.document.sentences)
        sentence_count = text_from_url.count('.')
    else:
        return None

    desired_sentence_count = round(sentence_count * ratio)

    if summarizer_to_use == "luhn": # Further development can check for other type of summarizers in the Sumy library
        summarizer = LuhnSummarizer()

    summary_tuple_list = summarizer(parser.document, desired_sentence_count)
    summary = ' '.join(str(sentence) for sentence in summary_tuple_list)

    return summary