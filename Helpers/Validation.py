import jsonschema
from Helpers.APIHelper import api_request_schema
from Helpers import APIHelper


def validate_api_request(request: object, required_properties: list) -> bool:
    json_content = APIHelper.fetch_request_json(request)

    if json_content is None: # Ensure a JSON request was posted
        return False

    if schema_validate(json_content) is False: # Validate the JSON request matches the defined schema/structure
        return False

    for property_name in required_properties: # Check if the API request contains the needed properties
        if not property_name in json_content:
            return False

    return True


def schema_validate(json) -> bool:
    try:
        jsonschema.validate(json, api_request_schema)
        return True
    except:
        return False
