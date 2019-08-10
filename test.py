import minio

m = minio.Minio(
    "192.168.1.121:9000",
    access_key="sssanikhani",
    secret_key="Sajjad326495S",
    secure=False
)
obj = m.fget_object("profileimages", "1.jpg", "/home/sss/sss/1.jpg")
print(bp)