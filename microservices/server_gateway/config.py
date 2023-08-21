import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

URL_FRONTEND = os.getenv("URL_FRONTEND", "")
API_MAX_REQUESTS_PER_DAY = int(os.getenv("API_MAX_REQUESTS_PER_DAY", "0"))
API_SECONDS_IN_DAY = int(os.getenv("API_SECONDS_IN_DAY", "0"))
GATEWAY_PORT = int(os.getenv("SERVER_GATEWAY_PORT", "0"))
REDIS_HOST = os.getenv("REDIS_HOST", "")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
SERVER_PROTOCOL = os.getenv("SERVER_PROTOCOL", "")
SERVER_JPG_HOST = "{}-jpg-service.image-converter-main".format(os.getenv("DOCKER_IMAGE_NAME", ""))
SERVER_JPG_PORT = os.getenv("SERVER_JPG_PORT", "")
SERVER_PNG_HOST = "{}-png-service.image-converter-main".format(os.getenv("DOCKER_IMAGE_NAME", ""))
SERVER_PNG_PORT = os.getenv("SERVER_PNG_PORT", "")
SERVER_WEBP_HOST = "{}-webp-service.image-converter-main".format(os.getenv("DOCKER_IMAGE_NAME", ""))
SERVER_WEBP_PORT = os.getenv("SERVER_WEBP_PORT", "")

__all__ = ["API_MAX_REQUESTS_PER_DAY", "API_SECONDS_IN_DAY", "REDIS_HOST", 
    "REDIS_PASSWORD", "GATEWAY_PORT", "SERVER_PROTOCOL", 
    "SERVER_JPG_HOST", "SERVER_JPG_PORT", "SERVER_PNG_HOST",
    "SERVER_PNG_PORT", "SERVER_WEBP_HOST", "SERVER_WEBP_PORT", "URL_FRONTEND"]