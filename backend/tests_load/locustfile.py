import tempfile
from PIL import Image
from locust import HttpLocust, task, between

class ImgToJPG(HttpLocust):
  wait_time = between(5, 15)

  @task
  def index(self):
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
          

class ImgToPNG(HttpLocust):
  wait_time = between(5, 15)

  @task
  def index(self):
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
          
class ImgToWEBP(HttpLocust):
  wait_time = between(5, 15)

  @task
  def index(self):
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