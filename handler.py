
from helper import json_response
from constant import HTTPStatus


class handlers:
    @staticmethod
    def generic_exception_handler(environ, start_response, exc: Exception):
        response = {
            "message": f"Error occurred: {str(exc)}"
        }
        return json_response(response,start_response,status = HTTPStatus.SERVER_ERROR)
    
    @staticmethod
    def url_not_found(path,start_response):
        response = {
            "message":"url nai"
        }
        return json_response(response,start_response,status=HTTPStatus.NOT_FOUND)