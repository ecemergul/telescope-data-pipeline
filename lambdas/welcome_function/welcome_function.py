import json

def lambda_handler(event, context):
    name = "ziyaretçi"

    if event.get("body"):
        body = json.loads(event["body"])
        name = body.get("name", name)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": f"<h1>Merhaba, {name}</h1>"
    }