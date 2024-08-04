import boto3
import base64

s3 = boto3.client('s3')


def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key = event["s3_key"]
    bucket = event["s3_bucket"]

    # Download the data from s3 to /tmp/image.png
    s3.download_file(bucket, key, "/tmp/image.png")

    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    return {
        "image_data": image_data,
        "s3_bucket": bucket,
        "s3_key": key,
        "inferences": []
    }


def test_lambda_handler():
    event = {
        "s3_bucket": "sagemaker-us-east-1-087802114688",
        "s3_key": "test/bicycle_s_000513.png"
    }
    lambda_handler(event, None)
