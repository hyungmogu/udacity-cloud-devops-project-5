import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SERVER_WEBP_PORT = int(os.getenv("SERVER_WEBP_PORT", "0"))
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")
AWS_OBJECT_EXPIRES_IN = os.getenv("AWS_OBJECT_EXPIRES_IN", "0")
TESTING = os.getenv("TESTING", "False").lower() == "true"