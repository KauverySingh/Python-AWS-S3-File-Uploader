import boto3

def upload_to_s3(file_path, bucket_name, object_name=None):
    """
    Uploads a file to an S3 bucket.
    :param file_path: Path to the file to upload.
    :param bucket_name: Name of the bucket to upload to.
    :param object_name: S3 object name. If not specified then file_name is used.
    :return: True if file was uploaded, else False.
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_path

    # Initialize the S3 client
    s3_client = boto3.client('s3')

    try:
        # Uploads the file
        response = s3_client.upload_file(file_path, bucket_name, object_name)
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False
    return True

# Example usage
file_path = 'C:\\Users\\Kauvery\\Documents\\About.txt'
bucket_name = 'bucketwithpython'
object_name = 'Readme.txt'

if upload_to_s3(file_path, bucket_name, object_name):
    print("File uploaded successfully.")
else:
    print("File upload failed.")
