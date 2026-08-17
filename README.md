# Cloud Backup Guardian

## Project Overview

Cloud Backup Guardian is an automated cloud backup and recovery system built using AWS services.

The system automatically detects files uploaded to a source Amazon S3 bucket, creates a backup in a separate backup S3 bucket, stores backup metadata in Amazon DynamoDB, monitors events using Amazon CloudWatch, and sends notifications through Amazon SNS.

## Objectives

- Automatically back up uploaded files
- Maintain a separate backup storage location
- Store backup metadata for tracking and recovery
- Monitor the backup process
- Provide notifications for backup events
- Improve data reliability and recovery

## AWS Services Used

- Amazon S3 – Source and backup file storage
- AWS Lambda – Automated backup processing
- Amazon DynamoDB – Backup metadata storage
- Amazon CloudWatch – Monitoring and logging
- Amazon SNS – Notifications
- AWS IAM – Permissions and access control

## Architecture

The project follows this workflow:

S3 Source Bucket
       ↓
AWS Lambda
       ↓
Backup S3 Bucket
       ↓
DynamoDB Metadata

CloudWatch monitors the Lambda execution and SNS can be used for notifications.

## Project Workflow

1. A file is uploaded to the source S3 bucket.
2. The S3 event triggers the Lambda function.
3. Lambda processes the uploaded file.
4. The file is copied to the backup S3 bucket.
5. Backup metadata is stored in DynamoDB.
6. CloudWatch records execution logs and monitoring information.
7. SNS can send notifications about backup events.

## Lambda Function

The main automation logic is implemented in:

`lambda-function.py`

The function handles the backup process and returns a success response when the backup is completed successfully.

## Dashboard

A project dashboard was designed to present the Cloud Backup Guardian system and its architecture.

Dashboard file:

`Cloud_Backup_Guardian_Dashboard.pdf`

## Project Status

- S3 backup workflow: Completed
- Lambda function: Completed
- DynamoDB metadata storage: Completed
- CloudWatch monitoring: Configured
- SNS notifications: Configured
- Project dashboard: Completed
- Documentation: Completed

## Repository Contents

- `lambda-function.py` – AWS Lambda backup function
- `Cloud_Backup_Guardian_Dashboard.pdf` – Project dashboard and architecture
- `README.md` – Project documentation

## Conclusion

Cloud Backup Guardian demonstrates how AWS serverless services can be integrated to create an automated, monitored, and reliable cloud backup solution.
