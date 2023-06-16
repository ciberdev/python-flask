"""Blueprint que describe las rutas del controlador de usuarios"""
from flask import Blueprint
from controllers.groups_controller import list, datos_grupo 

bpgroups = Blueprint('bpgroups', __name__)

bpgroups.route('/', methods=['GET', 'POST'])(list)
bpgroups.route('/group', methods=['GET', 'POST'])(datos_grupo)
