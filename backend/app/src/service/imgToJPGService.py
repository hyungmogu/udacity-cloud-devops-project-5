from PIL import Image
from io import BytesIO
import os
import logging
import boto3
import re
from uuid import uuid4
from time import time
from botocore.exceptions import ClientError

from src.service.convertService import ConvertService


AWS_S3_BUCKET = os.environ.get("AWS_S3_BUCKET", "")
AWS_OBJECT_EXPIRES_IN = int(os.environ.get("AWS_OBJECT_EXPIRES_IN", "0"))


class ImgToJPGService(ConvertService):
  def convert(self, img):
    pil_image = Image.open(img).convert("RGB")
    in_mem_file = BytesIO()
    pil_image.save(in_mem_file, format="JPEG")
    in_mem_file.seek(0)

    return in_mem_file

  def upload(self, new_img):
    s3_client = boto3.client("s3")

    file_name = "{}-{}.jpeg".format(time(), uuid4().hex)
    response = None

    try:
      s3_client.upload_fileobj(new_img, AWS_S3_BUCKET, file_name)

      response = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": AWS_S3_BUCKET, "Key": file_name},
        ExpiresIn=AWS_OBJECT_EXPIRES_IN,
      )

    except ClientError as e:
      logging.error(e)

    return response
