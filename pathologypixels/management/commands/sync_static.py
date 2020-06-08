import boto3
import mimetypes
import os

from django.core.management.base import BaseCommand
from django.conf import settings

s3 = boto3.client(
    "s3",
    endpoint_url='https://s3.us-west-1.amazonaws.com',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        static_folders = os.listdir(os.path.join(settings.BASE_DIR, 'static'))
        for folder in static_folders:
            if '.DS_Store' in folder:
                continue
            files = os.listdir(os.path.join(settings.BASE_DIR, 'static', folder))
            for file in files:
                if '.DS_Store' in file:
                    continue
                if os.path.isfile(os.path.join(settings.BASE_DIR, 'static', folder, file)):
                    s3_upload(file, folder+'/')


def s3_upload(file_name=None, folder_name=None, acl="public-read"):
    print(folder_name+file_name)
    file_data = open(os.path.join(settings.BASE_DIR, 'static', folder_name, file_name), 'rb')

    content_type = mimetypes.guess_type(os.path.join(settings.BASE_DIR, 'static', folder_name, file_name))
    print(content_type[0])
    file_upload = s3.put_object(
        Body=file_data,
        Bucket='ucsf-pathology',  # S3 bucket name
        Key='static/' + folder_name+file_name,
        ACL=acl,
        ContentType=content_type[0]
    )

    file_data.close()