import boto3
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f"INIT LAMBDA EXECUTION \n")
    logger.info(f"Received event: {event}")

    result = {
        'ok': 'ok'
    }

    try:
        __readBuckets()
        response = {
            'statusCode': 200,
            'body': result
        }

        return response

    except BaseException as err:
        logger.error(f"Bucket Name: {err}")
        raise err


def __readBuckets():
    logger.info('Init Read Buckets')
    s3 = boto3.resource('s3', endpoint_url='http://localhost:4566')
    for bucket in s3.buckets.all():
        name =  bucket.name
        logger.info(f"Bucket Name: {name}")
