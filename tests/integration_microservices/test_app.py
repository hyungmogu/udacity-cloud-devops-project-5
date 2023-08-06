import os
import unittest
import requests
import tempfile
from PIL import Image
from dotenv import find_dotenv, load_dotenv
import boto3

load_dotenv(find_dotenv())

AWS_S3_BUCKET = "image-converter-test"
os.environ["AWS_S3_BUCKET"] = AWS_S3_BUCKET
os.environ["AWS_ACCESS_KEY_ID"] = "test"
os.environ["AWS_SECRET_ACCESS_KEY"] = "test"


class TestSimplePositiveGatewayToServerJPG(unittest.TestCase):
    def setUp(self):
        self.s3_resource = boto3.resource('s3')
        self.s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)
        self.minikube_service_url = os.environ.get('MINIKUBE_SERVICE_URL', "")
        self.gateway_port = os.environ.get("GATEWAY_PORT", "")

        if len(self.minikube_service_url) == 0:
            raise Exception("MINIKUBE_SERVICE_URL environment variable is not set")

    def test_health_endpoint_successfully_returns_ok(self):
        response = requests.get(f"{self.minikube_service_url}:{self.gateway_port}/health", timeout=10)
        self.assertEqual(response.status_code, 200)
    
    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        with tempfile.NamedTemporaryFile(suffix=".png") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = requests.post(
                    f"{self.minikube_service_url}:{self.gateway_port}/convert/to-jpg", 
                    files={"image": ("test.png", img_data, "image/png")}, timeout=10)

                self.assertEqual(response.status_code, 201)

    def test_convert_method_returns_error_if_image_is_not_valid(self):
        with tempfile.NamedTemporaryFile(suffix=".txt") as txt_file:
            txt_file.write(b'INVALID_IMAGE_DATA')

            with open(txt_file.name, "rb") as txt_data:
                response = requests.post(
                    f"{self.minikube_service_url}:{self.gateway_port}/convert/to-jpg",
                    files={"image": ("test.txt", txt_data, "text/plain")}, timeout=10)

                self.assertEqual(response.status_code, 415)


class TestSimplePositiveGatewayToServerPNG(unittest.TestCase):
    def setUp(self):
        self.s3_resource = boto3.resource('s3')
        self.s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)
        self.minikube_service_url = os.environ.get('MINIKUBE_SERVICE_URL', "")
        self.gateway_port = os.environ.get("GATEWAY_PORT", "")

        if len(self.minikube_service_url) == 0:
            raise Exception("MINIKUBE_SERVICE_URL environment variable is not set")
    
    def test_health_endpoint_successfully_returns_ok(self):
        response = requests.get(f"{self.minikube_service_url}:{self.gateway_port}/health", timeout=10)
        self.assertEqual(response.status_code, 200)

    def test_convert_method_successfully_converts_a_valid_image_to_png(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = requests.post(
                    f"{self.minikube_service_url}:{self.gateway_port}/convert/to-png", 
                    files={"image": ("test.jpg", img_data, "image/jpg")}, timeout=10)

                self.assertEqual(response.status_code, 201)

    def test_convert_method_returns_error_if_image_is_not_valid(self):
        with tempfile.NamedTemporaryFile(suffix=".txt") as txt_file:
            txt_file.write(b'INVALID_IMAGE_DATA')

            with open(txt_file.name, "rb") as txt_data:
                response = requests.post(
                    f"{self.minikube_service_url}:{self.gateway_port}/convert/to-png",
                    files={"image": ("test.txt", txt_data, "text/plain")}, timeout=10)

                self.assertEqual(response.status_code, 415)


class TestSimplePositiveGatewayToServerWEBP(unittest.TestCase):
    def setUp(self):
        self.s3_resource = boto3.resource('s3')
        self.s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)
        self.minikube_service_url = os.environ.get('MINIKUBE_SERVICE_URL', "")
        self.gateway_port = os.environ.get("GATEWAY_PORT", "")

        if len(self.minikube_service_url) == 0:
            raise Exception("MINIKUBE_SERVICE_URL environment variable is not set")
    
    def test_health_endpoint_successfully_returns_ok(self):
        response = requests.get(f"{self.minikube_service_url}:{self.gateway_port}/health", timeout=10)
        self.assertEqual(response.status_code, 200)
        
    def test_convert_method_successfully_converts_a_valid_image_to_webp(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as img_file:
            img = Image.new("RGB", (50, 50), color="red")
            img.save(img_file.name)

            with open(img_file.name, "rb") as img_data:
                response = requests.post(
                    f"{self.minikube_service_url}:{self.gateway_port}/convert/to-webp", 
                    files={"image": ("test.jpg", img_data, "image/jpg")}, timeout=10)

                self.assertEqual(response.status_code, 201)

    def test_convert_method_returns_error_if_image_is_not_valid(self):
        with tempfile.NamedTemporaryFile(suffix=".txt") as txt_file:
            txt_file.write(b'INVALID_IMAGE_DATA')

            with open(txt_file.name, "rb") as txt_data:
                response = requests.post(
                    f"{self.minikube_service_url}:{self.gateway_port}/convert/to-webp",
                    files={"image": ("test.txt", txt_data, "text/plain")}, timeout=10)

                self.assertEqual(response.status_code, 415)
