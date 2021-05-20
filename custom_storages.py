from django.conf import Settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILE_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILE_LOCATION