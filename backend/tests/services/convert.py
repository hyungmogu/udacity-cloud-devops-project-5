import os
import requests
import unittest
import tempfile
import boto3
from moto import mock_s3
from io import BytesIO
from PIL import Image
from fastapi.testclient import TestClient

AWS_S3_BUCKET = "image-converter-test"
os.environ["AWS_S3_BUCKET"] = AWS_S3_BUCKET
os.environ["AWS_ACCESS_KEY_ID"] = "test"
os.environ["AWS_SECRET_ACCESS_KEY"] = "test"

from app import app
from src.services.convert import ImgToJPGService, ImgToPNGService, ImgToWEBPService

# HEALTH CHECK

class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def test_test_client_server_is_running(self):
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)

# TESTING IMG TO JPG SERVICE

@mock_s3
class TestSimplePositiveImgToJPGService(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)
        self.img_to_jpg_service = ImgToJPGService()
        s3_resource = boto3.resource('s3')
        s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        with tempfile.NamedTemporaryFile(suffix=".png") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = self.app.post("/convert/to-jpg",
                                         files={"image": ("test.png", img_data, "image/png")})

                self.assertEqual(response.status_code, 201)


@mock_s3
class TestSimpleNegativeImgToJPGService(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)
        self.img_to_jpg_service = ImgToJPGService()
        s3_resource = boto3.resource('s3')
        s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

    def test_if_convert_method_raises_exception_given_invalid_image_file_or_non_image(self):
        with tempfile.NamedTemporaryFile(suffix=".txt") as txt_file:
            txt_file.write(b'INVALID_IMAGE_DATA')

            response = self.app.post("/convert/to-jpg",
                                    files={"image": ("test.txt", txt_file, "text/plain")})
            self.assertEqual(response.status_code, 415)

    def test_upload_method_raises_exceptions_if_given_empty_data(self):
        response = self.app.post("/convert/to-jpg")
        self.assertEqual(response.status_code, 422) 

@mock_s3
class TestInputImgToJPGService(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)
        self.img_to_jpg_service = ImgToJPGService()
        s3_resource = boto3.resource('s3')
        s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

    def test_convert_method_converts_various_image_formats_to_jpg(self):
        for img_format in [".webp", ".png", ".jpg", ".jpeg"]:
            content_type = "image/{}".format(img_format[1:])
            with tempfile.NamedTemporaryFile(suffix=img_format) as img_file:
                img = Image.new("RGB", (50, 50), color="red")
                img.save(img_file.name)

                with open(img_file.name, "rb") as img_data:
                    response = self.app.post("/convert/to-jpg",
                                    files={"image": ("test{}".format(img_format), img_data, content_type)})
                    self.assertEqual(response.status_code, 201)

    def test_convert_method_handles_images_of_various_dimension_and_sizes(self):
        for image_size in [(50,200), (100,100), (250, 30)]:
            with tempfile.NamedTemporaryFile(suffix=".png") as img_file:
                tmp_img = Image.new("RGB", image_size, color="red")
                tmp_img.save(img_file.name)

                with open(img_file.name, "rb") as img_data:
                    response = self.app.post("/convert/to-jpg",
                                            files={"image": ("test.png", img_data, "image/png")})
                    self.assertEqual(response.status_code, 201)
                    self.assertIn("url", response.content)
                    
                    req = requests.get(response.json['url'])
                    img = Image.open(BytesIO(req.content))
                    self.assertEqual(image_size, img.size)


# class TestEdgeCaseImgToJPGService(unittest.TestCase):
#     def setUp(self):
#         self.app = TestClient(app)
#         self.img_to_jpg_service = ImgToJPGService()
    
#     def test_upload_method_raises_error_when_s3_bucket_is_not_available_or_accessible(self):
#         with tempfile.NamedTemporaryFile(suffix=".png") as img_file:
#             img = Image.new("RGB", (50, 50), color="red")
#             img.save(img_file.name)

#             with open(img_file.name, "rb") as img_data:
#                 response = self.app.post("/convert/to-jpg",
#                                          headers={"Content-Type": "multipart/form-data"},
#                                          data={"image": (BytesIO(img_data.read()), "test.png")})

#                 self.assertEqual(response.status_code, 500)
#                 self.assertIn("error", response.json)
    
# # TESTING IMG TO PNG SERVICE

# @mock_s3
# class TestSimplePositiveImgToPNGService(unittest.TestCase):
#     def setUp(self):
#         self.app = TestClient(app)
#         self.img_to_png_service = ImgToPNGService()
#         s3_resource = boto3.resource('s3')
#         s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

#     def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
#         with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
#             img = Image.new("RGB", (50, 50), color="red")
#             img.save(img_file.name)

#             with open(img_file.name, "rb") as img_data:
#                 response = self.app.post("/convert/to-png",
#                                          headers={"Content-Type": "multipart/form-data"},
#                                          data={"image": (BytesIO(img_data.read()), "test.jpg")})
 
#                 self.assertEqual(response.status_code, 200)
#                 self.assertIn("url", response.json)


# @mock_s3
# class TestSimpleNegativeImgToPNGService(unittest.TestCase):
#     def setUp(self):
#         self.app = TestClient(app)
#         self.img_to_png_service = ImgToPNGService()
#         s3_resource = boto3.resource('s3')
#         s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

#     def test_if_convert_method_raises_exception_given_invalid_image_file_or_non_image(self):
#         response = self.app.post("/convert/to-png",
#                                  headers={"Content-Type": "multipart/form-data"},
#                                  data={"image": (BytesIO(b"invalid_image_data"), "test.txt")})
#         self.assertEqual(response.status_code, 500)

#     def test_upload_method_raises_exceptions_if_given_empty_data(self):
#         response = self.app.post("/convert/to-png",
#                                  headers={"Content-Type": "multipart/form-data"})
#         self.assertEqual(response.status_code, 400) 

# @mock_s3
# class TestInputImgToPNGService(unittest.TestCase):
#     def setUp(self):
#         self.app = TestClient(app)
#         self.img_to_png_service = ImgToPNGService()
#         s3_resource = boto3.resource('s3')
#         s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

#     def test_convert_method_converts_various_image_formats_to_jpg(self):
#         for img_format in [".webp", ".png", ".jpg", ".jpeg"]:
#             with tempfile.NamedTemporaryFile(suffix=img_format) as img_file:
#                 img = Image.new("RGB", (50, 50), color="red")
#                 img.save(img_file.name)

#                 with open(img_file.name, "rb") as img_data:
#                     response = self.app.post("/convert/to-png",
#                                             headers={"Content-Type": "multipart/form-data"},
#                                             data={"image": (BytesIO(img_data.read()), "test{}".format(img_format))})
#                     self.assertEqual(response.status_code, 200)
#                     self.assertIn("url", response.json)

#     def test_convert_method_handles_images_of_various_dimension_and_sizes(self):
#         for image_size in [(50,200), (100,100), (250, 30)]:
#             with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
#                 tmp_img = Image.new("RGB", image_size, color="red")
#                 tmp_img.save(img_file.name)

#                 with open(img_file.name, "rb") as img_data:
#                     response = self.app.post("/convert/to-png",
#                                             headers={"Content-Type": "multipart/form-data"},
#                                             data={"image": (BytesIO(img_data.read()), "test.jpg")})
#                     self.assertEqual(response.status_code, 200)
#                     self.assertIn("url", response.json)
                    
#                     req = requests.get(response.json['url'])
#                     img = Image.open(BytesIO(req.content))
#                     self.assertEqual(image_size, img.size)


# class TestEdgeCaseImgToPNGService(unittest.TestCase):
#     def setUp(self):
#         self.app = TestClient(app)
#         self.img_to_png_service = ImgToPNGService()
    
#     def test_upload_method_raises_error_when_s3_bucket_is_not_available_or_accessible(self):
#         with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
#             img = Image.new("RGB", (50, 50), color="red")
#             img.save(img_file.name)

#             with open(img_file.name, "rb") as img_data:
#                 response = self.app.post("/convert/to-png",
#                                          headers={"Content-Type": "multipart/form-data"},
#                                          data={"image": (BytesIO(img_data.read()), "test.jpg")})

#                 self.assertEqual(response.status_code, 500)
#                 self.assertIn("error", response.json)
    
    
# # TESTING IMG TO WEBP SERVICE

# @mock_s3
# class TestSimplePositiveImgToWEBPService(unittest.TestCase):
#     def setUp(self):
#         self.app = TestClient(app)
#         self.img_to_webp_service = ImgToWEBPService()
#         s3_resource = boto3.resource('s3')
#         s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

#     def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
#         with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
#             img = Image.new("RGB", (50, 50), color="red")
#             img.save(img_file.name)

#             with open(img_file.name, "rb") as img_data:
#                 response = self.app.post("/convert/to-webp",
#                                          headers={"Content-Type": "multipart/form-data"},
#                                          data={"image": (BytesIO(img_data.read()), "test.jpg")})

#                 self.assertEqual(response.status_code, 200)
#                 self.assertIn("url", response.json)

# @mock_s3
# class TestSimpleNegativeImgToWEBPService(unittest.TestCase):
#     def setUp(self):
#         self.app = TestClient(app)
#         self.img_to_webp_service = ImgToWEBPService()
#         s3_resource = boto3.resource('s3')
#         s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

#     def test_if_convert_method_raises_exception_given_invalid_image_file_or_non_image(self):
#         response = self.app.post("/convert/to-webp",
#                                  headers={"Content-Type": "multipart/form-data"},
#                                  data={"image": (BytesIO(b"invalid_image_data"), "test.txt")})
#         self.assertEqual(response.status_code, 500)

#     def test_upload_method_raises_exceptions_if_given_empty_data(self):
#         response = self.app.post("/convert/to-webp",
#                                  headers={"Content-Type": "multipart/form-data"})
#         self.assertEqual(response.status_code, 400) 

# @mock_s3
# class TestInputImgToWEBPService(unittest.TestCase):
#     def setUp(self):
#         self.app = TestClient(app)
#         self.img_to_webp_service = ImgToWEBPService()
#         s3_resource = boto3.resource('s3')
#         s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)

#     def test_convert_method_converts_various_image_formats_to_jpg(self):
#         for img_format in [".webp", ".png", ".jpg", ".jpeg"]:
#             with tempfile.NamedTemporaryFile(suffix=img_format) as img_file:
#                 img = Image.new("RGB", (50, 50), color="red")
#                 img.save(img_file.name)

#                 with open(img_file.name, "rb") as img_data:
#                     response = self.app.post("/convert/to-webp",
#                                             headers={"Content-Type": "multipart/form-data"},
#                                             data={"image": (BytesIO(img_data.read()), "test{}".format(img_format))})
                    
#                     self.assertEqual(response.status_code, 200)
#                     self.assertIn("url", response.json)

#     def test_convert_method_handles_images_of_various_dimension_and_sizes(self):
#         for image_size in [(50,200), (100,100), (250, 30)]:
#             with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
#                 tmp_img = Image.new("RGB", image_size, color="red")
#                 tmp_img.save(img_file.name)

#                 with open(img_file.name, "rb") as img_data:
#                     response = self.app.post("/convert/to-webp",
#                                             headers={"Content-Type": "multipart/form-data"},
#                                             data={"image": (BytesIO(img_data.read()), "test.jpg")})
#                     self.assertEqual(response.status_code, 200)
#                     self.assertIn("url", response.json)
                    
#                     req = requests.get(response.json['url'])
#                     img = Image.open(BytesIO(req.content))
#                     self.assertEqual(image_size, img.size)


# class TestEdgeCaseImgToWEBPService(unittest.TestCase):
#     def setUp(self):
#         self.app = TestClient(app)
#         self.img_to_webp_service = ImgToWEBPService()
    
#     def test_upload_method_raises_error_when_s3_bucket_is_not_available_or_accessible(self):
#         with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
#             img = Image.new("RGB", (50, 50), color="red")
#             img.save(img_file.name)

#             with open(img_file.name, "rb") as img_data:
#                 response = self.app.post("/convert/to-webp",
#                                          headers={"Content-Type": "multipart/form-data"},
#                                          data={"image": (BytesIO(img_data.read()), "test.jpg")})

#                 self.assertEqual(response.status_code, 500)
#                 self.assertIn("error", response.json)
    
    
if __name__ == "__main__":
    unittest.main()