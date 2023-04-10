import os
import requests
import unittest
import tempfile
import boto3
from moto import mock_s3
from io import BytesIO
from PIL import Image

AWS_S3_BUCKET = "image-converter-test"
os.environ["AWS_S3_BUCKET"] = AWS_S3_BUCKET
os.environ["AWS_ACCESS_KEY_ID"] = "test"
os.environ["AWS_SECRET_ACCESS_KEY"] = "test"

from main import app
from src.service.ImgToPNGService import ImgToPNGService

@mock_s3
class TestSimplePositiveImgToPNGService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.img_to_png_service = ImgToPNGService()
        s3_resource = boto3.resource('s3')
        s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = self.app.post("/api/convert-to-png",
                                         content_type="multipart/form-data",
                                         data={"image": (BytesIO(img_data.read()), "test.jpg")})
                print(response)
                self.assertEqual(response.status_code, 200)
                self.assertIn("url", response.json)

@mock_s3
class TestSimpleNegativeImgToPNGService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.img_to_png_service = ImgToPNGService()
        s3_resource = boto3.resource('s3')
        s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

    def test_if_convert_method_raises_exception_given_invalid_image_file_or_non_image(self):
        response = self.app.post("/api/convert-to-png",
                                 content_type="multipart/form-data",
                                 data={"image": (BytesIO(b"invalid_image_data"), "test.txt")})
        self.assertEqual(response.status_code, 500)

    def test_upload_method_raises_exceptions_if_given_empty_data(self):
        response = self.app.post("/api/convert-to-png",
                                 content_type="multipart/form-data")
        self.assertEqual(response.status_code, 400) 

@mock_s3
class TestInputImgToPNGService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.img_to_png_service = ImgToPNGService()
        s3_resource = boto3.resource('s3')
        s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

    def test_convert_method_converts_various_image_formats_to_jpg(self):
        for img_format in [".webp", ".png", ".jpg", ".jpeg"]:
            with tempfile.NamedTemporaryFile(suffix=img_format) as img_file:
                img = Image.new("RGB", (50, 50), color="red")
                img.save(img_file.name)

                with open(img_file.name, "rb") as img_data:
                    response = self.app.post("/api/convert-to-png",
                                            content_type="multipart/form-data",
                                            data={"image": (BytesIO(img_data.read()), "test{}".format(img_format))})
                    self.assertEqual(response.status_code, 200)
                    self.assertIn("url", response.json)

    def test_convert_method_handles_images_of_various_dimension_and_sizes(self):
        for image_size in [(50,200), (100,100), (250, 30)]:
            with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
                tmp_img = Image.new("RGB", image_size, color="red")
                tmp_img.save(img_file.name)

                with open(img_file.name, "rb") as img_data:
                    response = self.app.post("/api/convert-to-png",
                                            content_type="multipart/form-data",
                                            data={"image": (BytesIO(img_data.read()), "test.jpg")})
                    self.assertEqual(response.status_code, 200)
                    self.assertIn("url", response.json)
                    
                    req = requests.get(response.json['url'])
                    img = Image.open(BytesIO(req.content))
                    self.assertEqual(image_size, img.size)


class TestEdgeCaseImgToPNGService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.img_to_png_service = ImgToPNGService()
    
    def test_upload_method_raises_error_when_s3_bucket_is_not_available_or_accessible(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = self.app.post("/api/convert-to-png",
                                         content_type="multipart/form-data",
                                         data={"image": (BytesIO(img_data.read()), "test.jpg")})
                print(response)
                self.assertEqual(response.status_code, 500)
                self.assertIn("error", response.json)
    
    
