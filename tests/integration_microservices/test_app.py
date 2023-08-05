import sys
import os
import unittest
import requests
from dotenv import find_dotenv, load_dotenv
import boto3

load_dotenv(find_dotenv())

AWS_S3_BUCKET = "image-converter-test"
os.environ["AWS_S3_BUCKET"] = AWS_S3_BUCKET
os.environ["AWS_ACCESS_KEY_ID"] = "test"
os.environ["AWS_SECRET_ACCESS_KEY"] = "test"

# Check if gateway to server-jpg works correctly
class TestSimplePositiveGatewayToServerJPG(unittest.TestCase):
    def setUp(self):
        self.s3_resource = boto3.resource('s3')
        self.s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)
        self.minikube_service_url = os.environ.get('MINIKUBE_SERVICE_URL', "")

        if len(self.minikube_service_url) == 0:
            raise Exception("MINIKUBE_SERVICE_URL environment variable is not set")
        
    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        pass        
    def test_convert_method_returns_error_if_image_is_not_valid(self):
        pass
# Check if gateway to server-png works correctly
class TestSimplePositiveGatewayToServerPNG(unittest.TestCase):
    def setUp(self):
        self.s3_resource = boto3.resource('s3')
        self.s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)
        self.minikube_service_url = os.environ.get('MINIKUBE_SERVICE_URL', "")

        if len(self.minikube_service_url) == 0:
            raise Exception("MINIKUBE_SERVICE_URL environment variable is not set")

    def test_convert_method_successfully_converts_a_valid_image_to_png(self):
        pass
    def test_convert_method_returns_error_if_image_is_not_valid(self):
        pass
# Check if gateway to server-webp works correctly
class TestSimplePositiveGatewayToServerWEBP(unittest.TestCase):
    def setUp(self):
        self.s3_resource = boto3.resource('s3')
        self.s3_resource.create_bucket(Bucket=AWS_S3_BUCKET)
        self.minikube_service_url = os.environ.get('MINIKUBE_SERVICE_URL', "")

        if len(self.minikube_service_url) == 0:
            raise Exception("MINIKUBE_SERVICE_URL environment variable is not set")
        
    def test_convert_method_successfully_converts_a_valid_image_to_webp(self):
        pass
    def test_convert_method_returns_error_if_image_is_not_valid(self):
        pass
