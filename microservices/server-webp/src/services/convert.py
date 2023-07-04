from PIL import Image
from io import BytesIO
import os
import logging
import boto3
from abc import ABC
from uuid import uuid4
from time import time
from botocore.exceptions import ClientError
from config import AWS_S3_BUCKET, AWS_OBJECT_EXPIRES_IN

class ConvertService(ABC):
  def upload(self, new_img, file_extension) -> dict:
    file_name = "{}-{}.{}".format(time(), uuid4().hex, file_extension)
    response = None

    try:
      s3_client = boto3.client("s3")
      s3_client.upload_fileobj(new_img, AWS_S3_BUCKET, file_name)

      response = s3_client.generate_presigned_url(
        "get_object",
        Params={"Bucket": AWS_S3_BUCKET, "Key": file_name},
        ExpiresIn=int(AWS_OBJECT_EXPIRES_IN)
      )

    except ClientError as e:
      logging.error(e)

    return response
  
class ImgToJPGService(ConvertService):
  def convert(self, buffer):
    pil_image = Image.open(buffer).convert("RGB")
    in_mem_file = BytesIO()
    pil_image.save(in_mem_file, format="jpeg")
    in_mem_file.seek(0)

    return in_mem_file
  
class ImgToPNGService(ConvertService):
  def convert(self, img):
    pil_image = Image.open(img).convert("RGB")
    in_mem_file = BytesIO()
    pil_image.save(in_mem_file, format="png")
    in_mem_file.seek(0)

    return in_mem_file
  
class ImgToWEBPService(ConvertService):
  def convert(self, img):
    pil_image = Image.open(img).convert("RGB")
    in_mem_file = BytesIO()
    pil_image.save(in_mem_file, format="webp")
    in_mem_file.seek(0)

    return in_mem_file