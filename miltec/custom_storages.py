# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    """
    Storage for uploaded media files.
    """
    location = settings.MEDIAFILES_LOCATION
