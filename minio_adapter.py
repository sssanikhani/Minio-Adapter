from hs_infra.meta_classes.singleton_meta_class import Singleton
import minio


class MinioAdapter(metaclass=Singleton):
    ACCESS_KEY = 'sssanikhani'
    SECRET_KEY = 'sssanikhani'
    HOST_NAME = '192.168.1.121'
    CONNECTION_PROTOCOL = "http://"

    def __init__(self):
        self.connection = self._get_connection()

    def _get_connection(self):
        return minio.Minio(
            self.HOST_NAME,
            access_key=self.ACCESS_KEY,
            secret_key=self.SECRET_KEY,
            secure=False
        )

    def download_object(self, bucket_name, object_name, file_path):
        if not self.connection.bucket_exists(bucket_name):
            return None
        try:
            self.connection.fget_object(bucket_name, object_name, file_path)
        except minio.error.NoSuchKey:
            return None

    def put_object(self, bucket_name, object_name, file_path):
        if not self.connection.bucket_exists(bucket_name):
            self.connection.make_bucket(bucket_name)
        return self.connection.fput_object(bucket_name, object_name, file_path)

    def get_objects_list(self, bucket_name):
        objects_list = []
        objects = self.connection.list_objects(bucket_name)
        for obj in objects:
            objects_list.append(obj.object_name)
        return objects_list

    def get_buckets_list(self, ):
        buckets_list = []
        buckets = self.connection.list_buckets()
        for bucket in buckets:
            buckets_list.append(bucket.name)
        return buckets_list
