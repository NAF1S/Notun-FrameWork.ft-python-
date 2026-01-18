import json

inventory = {
    "mobile" : [
        {"product id" : 1,"mobile_name":"samsung"},
        {"product id" : 2,"mobile_name":"apple"}
    ],
    "laptop" : [
        {"product id" : 1,"laptop_name":"dell"},
        {"product id" : 2,"laptop_name":"apple"}
    ]
}


raise RuntimeError("emnei error")
data = json.dumps(inventory)
print(data)
