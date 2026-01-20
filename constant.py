
inventory = {
    "mobile": [
        {"product_id": 1, "mobile_name": "samsung"},
        {"product_id": 2, "mobile_name": "apple"}
    ],
    "laptop": [
        {"product_id": 1, "laptop_name": "dell"},
        {"product_id": 2, "laptop_name": "apple"}
    ]
}

product = [
    {"product_id":1,"product_name":"apple"},
    {"product_id":2,"product_name":"dell"}
]

class HTTPStatus:
    OK = "200 OK"
    SERVER_ERROR = "500 Internal Server Error"
    NOT_FOUND = "404 NOT FOUND"
