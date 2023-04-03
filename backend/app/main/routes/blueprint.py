from flask import Blueprint
from controllers.imgToJPGControllers import ImgToJPGController
from controllers.imgToPNGControllers import ImgToPNGController
from controllers.imgToWEBPControllers import ImgToWEBPController

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/convert-to-jpg', methods=['POST'])(ImgToJPGController.create)
blueprint.route('/convert-to-png', methods=['POST'])(ImgToPNGController.create)
blueprint.route('/convert-to-webp', methods=['POST'])(ImgToWEBPController.create)