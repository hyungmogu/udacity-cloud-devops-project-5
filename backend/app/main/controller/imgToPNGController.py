from flask import request
from main.service.imgToPNGService import ImgToPNGService

def create_png():
  if (request.form.get("image") == None or request.form.get("image") == ""):
    return "Attached Image Empty", 500
  
  old_img = request.form.get("image")

  convert_service = ImgToPNGService()
  new_img = convert_service.convert(old_img)
  url = convert_service.upload(new_img)

  if url is None:
    return "Error", 500
  
  return url, 200