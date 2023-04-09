from flask import Blueprint
import src.controller.imgToJPGController as jpg
import src.controller.imgToPNGController as png
import src.controller.imgToWEBPController as webp

api = Blueprint('api', __name__, url_prefix='/api/')

api.route('/convert-to-jpg', methods=['POST'])(jpg.create_jpg)
api.route('/convert-to-png', methods=['POST'])(png.create_png)
api.route('/convert-to-webp', methods=['POST'])(webp.create_webp)
