import json

def lambda_handler(event, context):
    # Define your message here
    message = "This is a simple message."
    
    # Return the message
    return {
        'statusCode': 200,
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
