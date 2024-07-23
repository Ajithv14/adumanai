import boto3
from adumanai import app
s3_client = boto3.client('s3',
                        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY']) 


def upload_file_to_s3(file, file_name, bucket_name=app.config['S3_BUCKET'],folder_name = 'cakes', S3_LOCATION=f"https://{app.config['S3_BUCKET']}.s3.amazonaws.com/"):
    try:
        s3_client.upload_fileobj(
            file,
            bucket_name,
            f'{folder_name}/{file_name}',
            ExtraArgs={
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        print("Something Happened: ", e)
        return e
    
    return f"{S3_LOCATION}{folder_name}/{file_name}"