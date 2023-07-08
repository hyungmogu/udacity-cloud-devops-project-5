import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SERVER_WEBP_PORT = os.getenv("SERVER_WEBP_PORT", 8006)
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
AWS_OBJECT_EXPIRES_IN = os.getenv("AWS_OBJECT_EXPIRES_IN", "0")

__all__ = [AWS_S3_BUCKET, AWS_OBJECT_EXPIRES_IN]