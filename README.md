# Localstack with docker


## Initialize your project by running:

```bash
docker-compose  up
```

# List all buckets

```bash
aws --endpoint-url=http://localhost:4566 s3 ls
```

## Create bucket

```bash
aws --endpoint-url=http://localhost:4566 s3 mb s3://hmbucket
```

## Creating the folder on S3: a folder called “lambda” will be created

```bash
aws --endpoint-url=http://localhost:4566 s3api put-object --bucket hmbucket --key lambda
```

## Creating a queue in SQS
```bash
aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name lambda-tutorial
```



Reference:

https://www.serverless.com/plugins/serverless-localstack
https://danieldcs.com/simulando-aws-local-com-localstack-e-node-js/
https://blog.geekhunter.com.br/aws-lambda-python-pycharm-localstack/
https://levelup.gitconnected.com/run-go-aws-lambda-locally-with-localstack-and-serverless-framework-5c80894f389c