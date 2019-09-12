from jsonschema import validate

api_request_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://example.com/root.json",
    "type": "object",
    "required": [
        "user",
        "text"
    ],
    "properties": {
        "user": {"type": "string"},
        "text": {"type": "string"}
    }
}


def validate_request(json) -> object:
    try:
        validate(json, api_request_schema)
        return True
    except:
        return False
