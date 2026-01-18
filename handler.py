
from helper import json_response
from constant import HTTPStatus


class handlers:
    @staticmethod
    def generic_exception_handler(environ, start_response, exc: Exception):
        response = {
            "message": f"Error occurred: {str(exc)}"
        }
        return json_response(response,start_response,status = HTTPStatus.SERVER_ERROR)
