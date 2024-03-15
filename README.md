# Python-AWS-S3-File-Uploader

Simple Python File Uploader to AWS S3


This project provides a simple Python script to upload files from your local machine to an Amazon S3 bucket using the Boto3 library.

Prerequisites

1. AWS Account: You need an AWS account to use the S3 service. If you don't have one, you can sign up here.
2. Python: Ensure Python is installed on your system. You can download it from here.
3. Boto3 Library: Install the Boto3 library using pip:
pip install boto3

Setup

1. Create an S3 Bucket: Log in to your AWS Management Console, navigate to the S3 service, and create a bucket. Make sure to note down the bucket name.

2. AWS Credentials: Ensure you have your AWS Access Key ID and Secret Access Key ready. You can obtain these from the AWS IAM console.

Usage

1. Clone this repository or download the upload_to_s3.py file.

2. Open the upload_to_s3.py file in a text editor.

3. Replace the following placeholders in the script:

'path_to_your_local_file.txt': Path to the file you want to upload.
'your_bucket_name': Name of your S3 bucket.
'custom_name_for_uploaded_file.txt': Desired name for the file in the S3 bucket.

4. Save the changes.

5. Open a terminal or command prompt, navigate to the directory containing the upload_to_s3.py file, and run the script:
python upload_to_s3.py

6. Check the output to see if the file upload was successful.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.
