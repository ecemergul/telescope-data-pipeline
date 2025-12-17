import json

def lambda_handler(event, context):
    data = json.loads(event.get("body", "{}"))
    name = data.get("name", "ziyaretçi")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": f'<h1>Merhaba, "{name}"!</h1>'
    }