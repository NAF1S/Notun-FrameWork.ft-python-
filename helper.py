import json
from constant import HTTPStatus

def json_response(response_body, start_response, status=HTTPStatus.OK, headers=None):
    if headers is None:
        headers = []

    body = json.dumps(response_body)
    body_bytes = body.encode("utf-8")
    headers.append(('Content-Type', 'application/json'))
    headers.append(('Content-Length', str(len(body_bytes))))
    start_response(status, headers)
    return [body_bytes]
