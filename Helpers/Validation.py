from jsonschema import validate
from Helpers.APIHelper import api_request_schema


def summary_request(json, must_have_property=None) -> bool:
    try:
        validate(json, api_request_schema)

        if must_have_property is not None:
            property_populated = json[must_have_property]

            if not property_populated:  # checks if it's an empty string
                return False

        return True
    except:
        return False
