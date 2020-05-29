import os
import json
import xlrd
import boto3


def postprocess(event, context):
    """
    Function handler invoked each time one or more .xls
    files are uploaded on the configured S3 bucket.
    """ 
    print(f"Event dump: {json.dumps(event)}")
    
    s3 = boto3.resource("s3")
    sns = boto3.client("sns")

    for record in event["Records"]:
        # Download file from S3 to a local directory
        event_object = record["s3"]["object"]["key"]
        tmp_path = "/tmp/" + event_object        
        s3.Bucket(os.environ["BUCKET_NAME"]).download_file(event_object, tmp_path)
        
        # Analyze the spreadsheet content
        xl_workbook = xlrd.open_workbook(tmp_path)
        sheet_names = xl_workbook.sheet_names()

        # Send results via SNS
        sns.publish(
            TopicArn=os.environ["TOPIC_ARN"],
            Message=json.dumps(sheet_names),
            Subject="New XLS uploaded"
        )
