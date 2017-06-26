from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    location = 'static'


class MediaStorage(S3BotoStorage):
    location = 'media'
