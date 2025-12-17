import json

def lambda_handler(event, context):
    method = event["requestContext"]["http"]["method"]

    if method == "GET":
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": "<h1>Merhaba, ziyaretçi</h1>"
        }

    if method == "POST":
        body = json.loads(event.get("body", "{}"))
        name = body.get("name", "ziyaretçi")

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": f"<h1>Merhaba, {name}</h1>"
        }