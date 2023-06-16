"""Blueprint que describe las rutas del controlador de usuarios"""
from flask import Blueprint
from controllers.users_controller import list, datos_usuario 

bpusers = Blueprint('bpusers', __name__)

bpusers.route('/', methods=['GET', 'POST'])(list)
bpusers.route('/user', methods=['GET', 'POST'])(datos_usuario)
