"""Blueprint que describe las rutas del controlador de usuarios"""
from flask import Blueprint
from controllers.system_controller import login, inicio

bpsystem = Blueprint('bpsystem', __name__)

bpsystem.route('/', methods=['GET', 'POST'])(login)
bpsystem.route('/inicio', methods=['GET', 'POST'])(inicio)