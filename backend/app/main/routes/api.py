from flask import Blueprint
import main.controller.imgToJPGController as jpg
import main.controller.imgToPNGController as png
import main.controller.imgToWEBPController as webp

api = Blueprint('api', __name__)

api.route('/convert-to-jpg', methods=['POST'])(jpg.create_jpg)
api.route('/convert-to-png', methods=['POST'])(png.create_png)
api.route('/convert-to-webp', methods=['POST'])(webp.create_webp)