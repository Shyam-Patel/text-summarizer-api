

# JSON schema of incoming requests
api_request_schema = {
    "type": "object",
    "properties": {
        "user": {"type": "string"},
        "text": {"type": "string"},
        "url": {"type": "string"},
        "ratio": {"type": "number"}
    }
}

# HTTP response codes
success_code = 200
failure_code = 400


def fetch_request_json(request) -> object:
    if not request.is_json:
        return None

    return request.get_json()


def api_response(response_code: int, message: str) -> object:
    return {"status": response_code, "message": message}




