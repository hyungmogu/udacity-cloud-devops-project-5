from flask import request
from main.service.imgToWEBPService import ImgToWEBPService

def create_webp():
  old_img = request.form.get("image")

  convert_service = ImgToWEBPService()
  new_img = convert_service.convert(old_img)
  url = convert_service.upload(new_img)

  if url is None:
    return "Error", 500
  
  return url, 200