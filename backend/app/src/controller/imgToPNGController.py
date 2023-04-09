from flask import request, jsonify
from src.service.imgToPNGService import ImgToPNGService

def create_png():
  if (request.files["image"] == None or request.files["image"] == ""):
    return jsonify({"error": "Attached Image Empty"}), 500

  if not (request.files["image"].filename.endswith(".png") or request.files["image"].filename.endswith(".jpg") or request.files["image"].filename.endswith(".jpeg") or request.files["image"].filename.endswith(".png") or request.files["image"].filename.endswith(".webp") or request.files["image"].filename.endswith(".svg")):
    return jsonify({"error": "Incorrect File Format"}), 500
  
  old_img = request.files["image"]

  convert_service = ImgToPNGService()
  new_img = convert_service.convert(old_img)
  url = convert_service.upload(new_img)

  if url is None:
    return jsonify({"error": "Failed to upload image"}), 500
  
  return jsonify({"url": url}), 200