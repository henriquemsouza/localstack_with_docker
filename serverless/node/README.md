# LAMBDA NODE LOCAL WITH SERVERLESS AND LOCALSTACK


## Requirements:
```sh
npm i -g serverless
```

```sh
npm install --save-dev serverless-localstack
```
## Initialize your project by running:

```sh
serverless
```

## Test lambda with:
```sh
serverless invoke local --function=createUser  
```


aws --endpoint-url=http://localhost:4566 \
lambda create-function --function-name my-lambda \
--zip-file fileb://function.zip \
--handler index.handler --runtime nodejs12.x \
--role arn:aws:iam::000000000000:role/lambda-role 
