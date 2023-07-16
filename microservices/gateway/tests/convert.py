import unittest
import tempfile
from PIL import Image
from urllib.parse import urlparse
from fastapi.testclient import TestClient

from app import app
from config import SERVER_JPG_HOST, SERVER_JPG_PORT, SERVER_PNG_HOST, SERVER_PNG_PORT, SERVER_WEBP_HOST, SERVER_WEBP_PORT, SERVER_PROTOCOL

## JPG

# 1. check if sending a request to server-jpg has correct url. It's okay if response is not 200.
class TestSimplePositiveImgToJPG(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        with tempfile.NamedTemporaryFile(suffix=".png") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = self.app.post("/convert/to-jpg",
                                         files={"image": ("test.png", img_data, "image/png")})

                # check response url pathname is correct
                pathname = urlparse(response.url).path
                self.assertEqual(pathname, "/convert/to-jpg")

                # check if host is correct
                host = urlparse(response.url).netloc
                self.assertEqual(host, "{}:{}".format(SERVER_JPG_HOST, SERVER_JPG_PORT))

# 2. check if sending a request to server-jpg contains correct header. It's okay if response is not 200.

## PNG

# 1. check if sending a request to server-png has correct url. It's okay if response is not 200.
class TestSimplePositiveImgToPNG(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = self.app.post("/convert/to-png",
                                         files={"image": ("test.png", img_data, "image/jpg")})

                # check response url pathname is correct
                pathname = urlparse(response.url).path
                self.assertEqual(pathname, "/convert/to-png")

                # check if host is correct
                host = urlparse(response.url).netloc
                self.assertEqual(host, "{}:{}".format(SERVER_JPG_HOST, SERVER_JPG_PORT))

# 2. check if sending a request to server-png contains correct header. It's okay if response is not 200.

## WEBP

# 1. check if sending a request to server-webp has correct url. It's okay if response is not 200.

# 2. check if sending a request to server-webp contains correct header. It's okay if response is not 200.