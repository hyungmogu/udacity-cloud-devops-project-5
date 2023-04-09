import os
import unittest
import tempfile
from moto import mock_s3
from io import BytesIO
from PIL import Image

from app.main import app
from src.service.imgToJPGService import ImgToJPGService

class TestSimplePositiveImgToJPGService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.img_to_jpg_service = ImgToJPGService()

    @mock_s3
    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        with tempfile.NamedTemporaryFile(suffix=".png") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = self.app.post("/convert-to-jpg",
                                         content_type="multipart/form-data",
                                         data={"image": (BytesIO(img_data.read()), "test.png")})
                self.assertEqual(response.status_code, 200)
                self.assertIn("url", response.json)

class TestSimpleNegativeImgToJPGService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.img_to_jpg_service = ImgToJPGService()

    @mock_s3
    def test_if_convert_method_raises_exception_given_invalid_image_file_or_non_image(self):
        response = self.app.post("/convert-to-jpg",
                                 content_type="multipart/form-data",
                                 data={"image": (BytesIO(b"invalid_image_data"), "test.txt")})
        self.assertEqual(response.status_code, 500)

    def test_upload_method_raises_exceptions_when_trying_to_upload_invalid_file_to_s3(self):
        pass 

class TestInputImgToJPGService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.img_to_jpg_service = ImgToJPGService()

    def test_convert_method_converts_various_image_formats_to_jpg(self):
        pass

    def test_convert_method_handles_images_of_various_dimension_and_sizes(self):
        pass

class TestEdgeCaseImgToJPGService(unittest.TextCase):
    def setUp(self):
        self.app = app.test_client()
        self.img_to_jpg_service = ImgToJPGService()
    
    def test_upload_method_raises_error_when_s3_bucket_is_not_available_or_accessible(self):
        pass

    def test_upload_method_raises_error_when_s3_bucket_exceeds_maximum_number_of_storage_limit(self):
        pass

    def test_upload_method_when_aws_object_expires_in_value_is_negative_or_invalid(self):
        pass
    
