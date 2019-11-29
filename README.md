# Text Summarization API
> Web API for the text summarization project written in Python and utilizing the lightweight Flask framework.

### Setup
____
The following are the main packages used in the development of this API:
- Python 3.7
- Flask, Flask-Cors, Flask-RESTful
- gensim
- sumy

The full list is contained in `requirements.txt`. Running the following command will install them:

`$ pip install -r requirements.txt`

### API Guide
___
All requests must be in JSON format. Currently, the API will validate the request object and it will reject the request if it doesn't meet the following format:

{<br/>
    "text" : "string", <br/>
    "url" : "string", <br/>
    "ratio" : "number" <br/>
}

- the ratio must be between 0 and 1 ( [percent/100] reduction of the text )
- you must supply either the text or the url

#### API Endpoints:
`/textrank/text` <br/>
The API request must have the "text" property populated

`/textrank/url` <br/>
The API request must have the "url" property populated

`/luhn/text` <br/>
The API request must have the "text" property populated

`/luhn/url` <br/>
The API request must have the "url" property populated



