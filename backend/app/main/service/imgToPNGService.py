from PIL import Image
from io import BytesIO
import base64
import os
import logging
import boto3
from uuid import uuid4
from time import time
from botocore.exceptions import ClientError

from main.service.convertService import ConvertService


AWS_S3_BUCKET = os.environ.get("AWS_S3_BUCKET", "")
AWS_OBJECT_EXPIRES_IN = int(os.environ.get("AWS_OBJECT_EXPIRES_IN", "0"))


class ImgToPNGService(ConvertService):
  def convert(self, img):
    pil_image = Image.open(img).convert("RGB")
    in_mem_file = BytesIO()
    pil_image.save(in_mem_file, format="png")
    in_mem_file.seek(0)

    return in_mem_file

  def upload(self, new_img):
    s3_client = boto3.client("s3")

    object_name = "{}-{}.png".format(int(time(), uuid4().hex))
    response = None

    try:
      s3_client.upload_file(new_img, AWS_S3_BUCKET, object_name)

      response = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": AWS_S3_BUCKET, "Key": object_name},
        ExpiresIn=AWS_OBJECT_EXPIRES_IN,
      )

    except ClientError as e:
      logging.error(e)

    return response
