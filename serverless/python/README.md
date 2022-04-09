# LAMBDA PYTHON LOCAL WITH SERVERLESS AND LOCALSTACK


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
serverless invoke local  --function main
```

### Response: 
```json
{
    "statusCode": 200,
    "body": "{\"result\": true}"
}
```

Reference:

[Serverless](https://www.serverless.com/plugins/serverless-localstack)