from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_session import Session
from routes.bpusers import bpusers
from routes.bpsystem import bpsystem

def create_app():
    """Funcion de creacion de una aplicacion Flask"""
    newapp = Flask(__name__)
    # Seleccionamos el objeto de configuracion de acuerdo a lo que estemos haciendo (DEV, PROD, TEST)
    newapp.config.from_object('config.DevConfig')
    
    # Definimos los blueprints que invocaran a nuestros controllers, de acuerdo a la URL que haya sido invocada.
    newapp.register_blueprint(bpsystem, url_prefix='/')
    newapp.register_blueprint(bpusers, url_prefix='/users')
    
    return newapp

app = create_app()
bootstrap  = Bootstrap5(app)
Session(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')