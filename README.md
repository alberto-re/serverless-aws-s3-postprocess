# serverless-aws-s3-postprocess

An example of how to postprocess Excel files uploaded to S3 using the Serverless Framework.

For the sake of example uploaded files are opened using the library _xlrd_ and the name of the sheets found are sent by mail to all the subscribers of a target SNS topic.

## Prerequisites

- Install the serverless framework

```
npm install serverless -g
```

- Install the _serverless-python-requirements_ plugin

```
npm install
```

- Configure your AWS credentials through [one of the provided methods](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

- Edit the _serverless.yml_ file and insert desided values for the variables under the _custom_ section 

## Deploy

By default it deploys on the _dev_ stage. To deploy in another stage use the _--stage_ parameter.

```
serverless deploy [--stage <STAGE>]
```
