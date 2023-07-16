import os
import unittest
import tempfile
import boto3
from moto import mock_s3
from PIL import Image
from fastapi.testclient import TestClient

AWS_S3_BUCKET = "image-converter-test"
os.environ["AWS_S3_BUCKET"] = AWS_S3_BUCKET
os.environ["AWS_ACCESS_KEY_ID"] = "test"
os.environ["AWS_SECRET_ACCESS_KEY"] = "test"

from app import app
from src.services.convert import ImgToWEBPService


@mock_s3
class TestSimplePositiveImgToWEBPService(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)
        self.img_to_webp_service = ImgToWEBPService()
        s3_resource = boto3.resource('s3')
        s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = self.app.post("/convert/to-webp",
                                         files={"image": ("test.jpg", img_data, "image/jpg")})

                self.assertEqual(response.status_code, 201)

@mock_s3
class TestSimpleNegativeImgToWEBPService(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)
        self.img_to_webp_service = ImgToWEBPService()
        s3_resource = boto3.resource('s3')
        s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

    def test_if_convert_method_raises_exception_given_invalid_image_file_or_non_image(self):
        with tempfile.NamedTemporaryFile(suffix=".txt") as txt_file:
            txt_file.write(b'INVALID_IMAGE_DATA')

            response = self.app.post("/convert/to-webp",
                                    files={"image": ("test.txt", txt_file, "text/plain")})
            self.assertEqual(response.status_code, 415)

    def test_upload_method_raises_exceptions_if_given_empty_data(self):
        response = self.app.post("/convert/to-webp")
        self.assertEqual(response.status_code, 422) 

@mock_s3
class TestInputImgToWEBPService(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)
        self.img_to_webp_service = ImgToWEBPService()
        s3_resource = boto3.resource('s3')
        s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

    def test_convert_method_converts_various_image_formats_to_webp(self):
        for img_format in [".webp", ".png", ".jpg", ".jpeg"]:
            content_type = "image/{}".format(img_format[1:])
            with tempfile.NamedTemporaryFile(suffix=img_format) as img_file:
                img = Image.new("RGB", (50, 50), color="red")
                img.save(img_file.name)

                with open(img_file.name, "rb") as img_data:
                    response = self.app.post("/convert/to-webp",
                                            files={"image": ("test{}".format(img_format), img_data, content_type)})
                    self.assertEqual(response.status_code, 201)

    def test_convert_method_handles_images_of_various_dimension_and_sizes(self):
        for image_size in [(50,200), (100,100), (250, 30)]:
            with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
                tmp_img = Image.new("RGB", image_size, color="red")
                tmp_img.save(img_file.name)

                with open(img_file.name, "rb") as img_data:
                    response = self.app.post("/convert/to-webp",
                                            files={"image": ("test.jpg", img_data, "image/jpg")})
                    self.assertEqual(response.status_code, 201)
                    self.assertTrue(len(response.content) > 0)
                    
                    # req = requests.get(response.json['url'])
                    # img = Image.open(BytesIO(req.content))
                    # self.assertEqual(image_size, img.size)

class TestEdgeCaseImgToWEBPService(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)
        self.img_to_webp_service = ImgToWEBPService()
    
    def test_upload_method_raises_error_when_s3_bucket_is_not_available_or_accessible(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = self.app.post("/convert/to-webp",
                                         files={"image": ("test.jpg", img_data, "image/jpg")})

                self.assertEqual(response.status_code, 500)
    
    
if __name__ == "__main__":
    unittest.main()