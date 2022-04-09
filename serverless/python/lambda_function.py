


def lambda_handler(event, context):
    print(f"Received event: {event}")

    result = {
        'ok': 'ok'
    }

    response = {
        'statusCode': 200,
        'body': result
    }

    return response