from constant import inventory
from helper import json_response
from middleware import Middleware
from handler import handlers


class Application:
    def __init__(self):
        pass
    def __call__(self, environ,start_response,*args, **kwds):
        path = environ.get("PATH_INFO","/")
        segments = [s for s in path.split("/") if s]
        category = segments[-1] if segments else ""
        product = inventory.get(category,[])
        return json_response(product,start_response)
    
app = Application()

middleware =  Middleware(app,handlers.generic_exception_handler)