from flask import request
from src.service.imgToJPGService import ImgToJPGService

def create_jpg():

  if (request.files["image"] == None or request.files["image"] == ""):
    return "Attached Image Empty", 500
  
  if not (request.files["image"].filename.endswith(".png") or request.files["image"].filename.endswith(".jpg") or request.files["image"].filename.endswith(".jpeg") or request.files["image"].filename.endswith(".png") or request.files["image"].filename.endswith(".webp") or request.files["image"].filename.endswith(".svg")):
    return "Incorrect File Format", 500

  old_img = request.files["image"]

  convert_service = ImgToJPGService()
  new_img = convert_service.convert(old_img)
  url = convert_service.upload(new_img)

  if url is None:
    return "Error", 500
  
  return url, 200