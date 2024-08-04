import json

THRESHOLD = .7


def lambda_handler(event, context):
    # Grab the inferences from the event
    inferences = event["inferences"]
    if isinstance(inferences, str):
        inferences = json.loads(inferences)

    # Check if any values in our inferences are above THRESHOLD
    threshold = event.get("threshold", THRESHOLD)
    meets_threshold = any([float(x) > threshold for x in inferences])

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if not meets_threshold:
        raise Exception(f"THRESHOLD_CONFIDENCE_NOT_MET: {inferences}")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }

def test_lambda_handler():
    event = {
        "inferences": [
            0.99,
            0.01
        ]
    }

    assert lambda_handler(event, None)
