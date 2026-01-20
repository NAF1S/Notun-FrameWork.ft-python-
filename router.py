
from helper import json_response
from constant import inventory
from handler import handlers
from webob import Response, Request
from parse import parse
class RouteManager:

    def __init__(self):
        self.route = {}

    def register(self, path, handler):
        if path in self.route:
            raise RuntimeError(f"Path :{path} use kora hoye gese")
        else:
            self.route[path] = handler

    def dispatch(self, environ, start_response):
        http_request = Request(environ)
        handler, kwargs = self.find_handler(http_request.path)
        if handler is None:
            return handlers.url_not_found(http_request.path, start_response)
        result = handler(http_request, **kwargs)
        if isinstance(result, Response):
            return result(environ, start_response)
        return result
    
    def find_handler(self,given_path)->tuple:
        for path,handler in self.route.items():
            parsed = parse(path,given_path)
            if parsed:
                return handler,parsed.named
        return None, {}