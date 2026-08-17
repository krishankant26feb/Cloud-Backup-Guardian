# Cloud Backup Guardian

## Project Overview

Cloud Backup Guardian is an automated cloud backup and recovery system built using AWS services. The system automatically detects files uploaded to a Source S3 Bucket, creates a backup in a separate Backup S3 Bucket, stores backup metadata in DynamoDB, monitors events using CloudWatch, and sends notifications through Amazon SNS.

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch
- Amazon SNS
- AWS IAM

## System Architecture

User → Source S3 Bucket → AWS Lambda → Backup S3 Bucket → DynamoDB → CloudWatch → Amazon SNS

## How It Works

1. A user uploads a file to the Source S3 Bucket.
2. The S3 upload event triggers the AWS Lambda function.
3. Lambda detects the newly uploaded file.
4. Lambda copies the file to the Backup S3 Bucket.
5. Backup metadata is stored in DynamoDB.
6. CloudWatch records the backup events and Lambda execution logs.
7. Amazon SNS sends notifications for backup success or failure.
8. Files can be restored from the Backup Bucket when required.

## Backup Metadata

The system records:

- File Name
- Upload Time
- Backup Status
- File Size
- Timestamp
- Recovery Status

## Monitoring and Validation

The system validates that:

- Uploaded files are automatically backed up.
- Duplicate uploads can be detected using file metadata.
- Backup events are logged in CloudWatch.
- Backup success and failure events can generate SNS notifications.
- Files can be restored from the Backup Bucket.

## Project Deliverables

### Python Lambda Script

AWS Lambda function developed using Python and boto3.

### Dashboard

The project dashboard was developed using Wix.

Dashboard PDF:

`Cloud_Backup_Guardian_Dashboard.pdf`

### Architecture Diagram

The architecture diagram represents the complete AWS backup workflow.

### Backup Report

The backup report contains:

- File Name
- Upload Time
- Backup Status
- Recovery Status
- Timestamp

## Testing

Multiple files were uploaded to the Source S3 Bucket to validate the backup workflow.

The following were verified:

- Automatic file backup
- Metadata storage
- CloudWatch logging
- SNS notification workflow
- File recovery from the Backup Bucket

## Project Status

Project completed and tested as part of the internship project submission.

## Author

Krishan Kant
