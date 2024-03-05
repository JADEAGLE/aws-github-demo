import json

def lambda_handler(event, context):
    # Define your message here
    message = "Tomorrow is Donut day!"
    
    # Return the message
    return {
        'statusCode': 200,
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
