import sys
from flask import request
from main.service.imgToJPGService import ImgToJPGService

def create_jpg():
  if (request.form.get("image") == None or request.form.get("image") == ""):
    return "Attached Image Empty", 500

  old_img = request.form.get("image")

  convert_service = ImgToJPGService()
  new_img = convert_service.convert(old_img)
  url = convert_service.upload(new_img)

  if url is None:
    return "Error", 500
  
  return url, 200