import json
from helper import json_response
from constant import product, HTTPStatus,inventory
from app import app
from webob import Request, Response

@app.route('/product')
def get_product(request: Request):
    body = json.dumps(inventory)
    return Response(body, status=HTTPStatus.OK)

@app.route('/product/{category}')
def get_product_by_category(request:Request,category:str)->Response:
    if category not in inventory:
        return Response(
            json_body = {
                "message":"category nai :/"
            }
            ,status=HTTPStatus.NOT_FOUND
        )
    body = json.dumps(inventory.get(category))
    return Response(body=body,status=HTTPStatus.OK)