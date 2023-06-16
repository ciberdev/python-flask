from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_session import Session
from routes.bpusers import bpusers
from routes.bpgroups import bpgroups
from routes.bpsystem import bpsystem
from flask_sqlalchemy import SQLAlchemy
from lib.dbconnection import db

def create_app():
    """Funcion de creacion de una aplicacion Flask"""
    newapp = Flask(__name__)
    # Seleccionamos el objeto de configuracion de acuerdo a lo que estemos haciendo (DEV, PROD, TEST)
    newapp.config.from_object('config.DevConfig')
    db.init_app(newapp)
    
    # Definimos los blueprints que invocaran a nuestros controllers, de acuerdo a la URL que haya sido invocada.
    newapp.register_blueprint(bpsystem, url_prefix='/')
    newapp.register_blueprint(bpusers, url_prefix='/users')
    newapp.register_blueprint(bpgroups, url_prefix='/groups')
    
    return newapp

app = create_app()
#db = SQLAlchemy(app)
bootstrap  = Bootstrap5(app)
Session(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')