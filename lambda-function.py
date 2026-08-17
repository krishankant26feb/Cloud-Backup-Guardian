import boto3
import urllib.parse
from datetime import datetime, timezone

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")

BACKUP_BUCKET = "krishan-aws-project2-2026"
TABLE_NAME = "backupmetadata"

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):

    print("Backup process started")
    print("Received event:", event)

    try:
        # Get S3 event information
        record = event["Records"][0]

        source_bucket = record["s3"]["bucket"]["name"]
        file_key = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        print(f"Source bucket: {source_bucket}")
        print(f"File: {file_key}")

        # Get file information
        head = s3.head_object(
            Bucket=source_bucket,
            Key=file_key
        )

        file_size = head["ContentLength"]
        upload_time = datetime.now(timezone.utc).isoformat()

        # Check duplicate
        existing = table.get_item(
            Key={"file_name": file_key}
        )

        if "Item" in existing:
            print(f"Duplicate upload detected: {file_key}")

            return {
                "statusCode": 200,
                "body": f"Duplicate file detected: {file_key}"
            }

        # Copy file to backup bucket
        s3.copy_object(
            Bucket=BACKUP_BUCKET,
            CopySource={
                "Bucket": source_bucket,
                "Key": file_key
            },
            Key=file_key
        )

        print(f"Backup successful: {file_key}")

        # Store metadata in DynamoDB
        table.put_item(
            Item={
                "file_name": file_key,
                "UploadTime": upload_time,
                "BackupStatus": "SUCCESS",
                "FileSize": file_size
            }
        )

        print("Metadata saved to DynamoDB")

        return {
            "statusCode": 200,
            "body": f"Backup successful: {file_key}"
        }

    except Exception as e:

        print("Backup failed!")
        print(str(e))

        return {
            "statusCode": 500,
            "body": f"Backup failed: {str(e)}"
        }
