#
#  Ejercicio
#  1. Crear una rutina que permita leer una opcion seleccionada por el usuario de un menu.
#  2. Ejecutar la opcion
#

from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import sessionmaker
from config import Config
from controllers import UsersController
from entities.base import Base


def menuPrincipal(session):
    fin = 0
    servicio = UsersController()
    while (fin == 0 ):
        print("1. Crear usuario, 2. Crear tipo de usuario, 3. Crear grupo 4. Listar usuarios 0. Salir")
        opcion = int(input("Ingrese la opcion:"))         
        if(opcion == 1):
            servicio.crearUsuario(session)
        elif(opcion == 4):
            servicio.mostrarUsuarios(session)
        elif(opcion == 0):
            fin = 1
            
if __name__ == "__main__":
    
    # Creamos una conexion a la base de datos mediante la funcion create_engine.
    config = Config()
    engine = create_engine(f"mssql+pymssql://{config.username}:{config.password}@{config.server}/{config.database}")    
    Base.metadata.bind = engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
    session = SessionLocal()     
    
    menuPrincipal(session)            