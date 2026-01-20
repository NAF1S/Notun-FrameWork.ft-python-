from constant import inventory
from helper import json_response
from middleware import Middleware
from handler import handlers
from router import RouteManager
from webob import Request,Response

class Application:
    def __init__(self):
        self.router = RouteManager()
    def __call__(self, environ,start_response):
        return self.router.dispatch(environ,start_response)
    
    def route(self,path):
        def dec(handler):
            self.router.register(path,handler)
            return handler
        return dec
    
app = Application()

middleware =  Middleware(app,handlers.generic_exception_handler)