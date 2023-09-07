import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

URL_FRONTEND = os.getenv("URL_FRONTEND", "")
GATEWAY_PORT = int(os.getenv("SERVER_GATEWAY_PORT", "0"))
SERVER_PROTOCOL = os.getenv("SERVER_PROTOCOL", "")
SERVER_JPG_HOST = "{}-jpg-service".format(os.getenv("DOCKER_IMAGE_NAME", ""))
SERVER_JPG_PORT = os.getenv("SERVER_JPG_PORT", "")
SERVER_PNG_HOST = "{}-png-service".format(os.getenv("DOCKER_IMAGE_NAME", ""))
SERVER_PNG_PORT = os.getenv("SERVER_PNG_PORT", "")
SERVER_WEBP_HOST = "{}-webp-service".format(os.getenv("DOCKER_IMAGE_NAME", ""))
SERVER_WEBP_PORT = os.getenv("SERVER_WEBP_PORT", "")

__all__ = ["GATEWAY_PORT", "SERVER_PROTOCOL",
    "SERVER_JPG_HOST", "SERVER_JPG_PORT", "SERVER_PNG_HOST",
    "SERVER_PNG_PORT", "SERVER_WEBP_HOST", "SERVER_WEBP_PORT", "URL_FRONTEND"]