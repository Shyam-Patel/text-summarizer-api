from jsonschema import validate

api_request_schema = {
    "user": "string",
    "text": "string"
}


def validate_request(json):
    validate(json, api_request_schema)
