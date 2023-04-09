import unittest
from app.main import app
from src.service.imgToJPGService import ImgToJPGService

class TestSimplePositiveImgToJPGService(unittest.TestCase):
    def setUp(self):
        pass

    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        pass

    def test_upload_method_uploads_converted_image_to_s3_bucket_and_returns_url(self):
        pass


class TestSimpleNegativeImgToJPGService(unittest.TestCase):
    def setUp(self):
        pass

    def test_if_convert_method_raises_exception_given_invalid_image_file_or_non_image(self):
        pass

    def test_upload_method_raises_exceptions_when_trying_to_upload_invalid_file_to_s3(self):
        pass 

class TestInputImgToJPGService(unittest.TestCase):
    def setUp(self):
        pass

    def test_convert_method_converts_various_image_formats_to_jpg(self):
        pass

    def test_convert_method_handles_images_of_various_dimension_and_sizes(self):
        pass

class TestEdgeCaseImgToJPGService(unittest.TextCase):
    def setUp(self):
        pass
    
    def test_upload_method_raises_error_when_s3_bucket_is_not_available_or_accessible(self):
        pass

    def test_upload_method_raises_error_when_s3_bucket_exceeds_maximum_number_of_storage_limit(self):
        pass

    def test_upload_method_when_aws_object_expires_in_value_is_negative_or_invalid(self):
        pass
    
