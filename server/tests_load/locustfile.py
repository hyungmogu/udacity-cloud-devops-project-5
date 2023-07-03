import tempfile
from PIL import Image
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
  wait_time = between(5, 15)

  @task
  def convert_to_jpg(self):
    for img_format in ['.webp', '.png', '.jpg', '.jpeg']:
      content_type = 'image/{}'.format(img_format[1:])
      with tempfile.NamedTemporaryFile(suffix=img_format) as \
        img_file:
        img = Image.new('RGB', (50, 50), color='red')
        img.save(img_file.name)

        with open(img_file.name, 'rb') as img_data:
          response = self.client.post('/convert/to-jpg',
              files={'image': ('test{}'.format(img_format),
              img_data, content_type)})
          
  @task
  def convert_to_png(self):
    for img_format in ['.webp', '.png', '.jpg', '.jpeg']:
      content_type = 'image/{}'.format(img_format[1:])
      with tempfile.NamedTemporaryFile(suffix=img_format) as \
        img_file:
        img = Image.new('RGB', (50, 50), color='red')
        img.save(img_file.name)

        with open(img_file.name, 'rb') as img_data:
          response = self.client.post('/convert/to-png',
              files={'image': ('test{}'.format(img_format),
              img_data, content_type)})
          
  @task
  def convert_to_webp(self):
    for img_format in ['.webp', '.png', '.jpg', '.jpeg']:
      content_type = 'image/{}'.format(img_format[1:])
      with tempfile.NamedTemporaryFile(suffix=img_format) as \
        img_file:
        img = Image.new('RGB', (50, 50), color='red')
        img.save(img_file.name)

        with open(img_file.name, 'rb') as img_data:
          response = self.client.post('/convert/to-webp',
              files={'image': ('test{}'.format(img_format),
              img_data, content_type)})