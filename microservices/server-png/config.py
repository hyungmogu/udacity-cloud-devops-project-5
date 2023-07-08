import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SERVER_PNG_PORT = os.getenv("SERVER_PNG_PORT", 8005)
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
AWS_OBJECT_EXPIRES_IN = os.getenv("AWS_OBJECT_EXPIRES_IN", "0")

__all__ = [AWS_S3_BUCKET, AWS_OBJECT_EXPIRES_IN]