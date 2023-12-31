"""Blueprint que describe las rutas del controlador de usuarios"""
from flask import Blueprint
from controllers.system_controller import login, inicio, logout

bpsystem = Blueprint('bpsystem', __name__)

bpsystem.route('/', methods=['GET', 'POST'])(login)
bpsystem.route('/inicio', methods=['GET', 'POST'])(inicio)
bpsystem.route('/logout', methods=['GET', 'POST'])(logout)
