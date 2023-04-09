import unittest
from main.service.imgToJPGService import ImgToJPGService

class ImgToJPGServiceSimplePositiveTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_convert_method_successfully_converts_a_valid_image_to_jpg(self):
        pass

    def test_upload_method_uploads_converted_image_to_s3_bucket_and_returns_url(self):
        pass


class ImgToJPGServiceSimpleNegativeTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_if_convert_method_raises_exception_given_invalid_image_file_or_non_image(self):
        pass

    def test_upload_method_raises_exceptions_when_trying_to_upload_invalid_file_to_s3(self):
        pass 

class ImgToJOGServiceInputPositiveTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_convert_method_converts_various_image_formats_to_jpg(self):
        pass
    
