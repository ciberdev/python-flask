from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import pyodbc
import datetime

from entities import User, UserType
from entities.base import Base

def insertarTiposUsuario(db):    
    tipoUsuario = UserType(idtype=None, utype_name="Externo")
    db.add(tipoUsuario)
    db.commit()

def insertarUsuarios(db, utype):    
    usuario = User(id=None, user_name="edugomez", email_address="edugomez@claro.com.gt",
                   password="secreto", first_name="Edu", last_name="Gomez", created=datetime.datetime.now(),
                   idtype=utype.idtype)
    db.add(usuario)
    db.commit()

if __name__ == "__main__":
    # Establecemos la conexión con SQL Server
    
    # Establecemos los parametros que vamos a ocupar para conectarnos a la base de datos
    server = '127.0.0.1'
    database = 'tutorial'
    username = 'tester'
    password = 'tester2023#'
    driver = 'FreeTDS'
    driver2 = 'ODBC Driver 17 for SQL Server'
    
    # Creamos una conexion a la base de datos mediante la funcion create_engine.
    engine = create_engine(f"mssql+pymssql://{username}:{password}@{server}/{database}")
    # Alternativamente...
    #engine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver2}")
    
    # Creamos una session
    Base.metadata.bind = engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
    session = SessionLocal()   
 
    # 1. Insertamos tipo de usuario   
    #insertarTiposUsuario(session)
    
    # 2. Seleccionamos el primer tipo de usuario en la tabla, para utilizarlo en la creacion de usuarios
    statement = select(UserType)
    tipousuario = session.execute(statement).fetchone().UserType
    
    # 3.  Teniendo el tipo de usuario, procedemos a insertar un nuevo usuario
    insertarUsuarios(session, tipousuario)
      
    # 4.  Realizamos una consulta a la tabla de usuarios y desplegamos su contenido.
    statement = select(User)
    resultado = session.execute(statement).all()
    
    print("Listado de usuarios en la BD:")
    for user in resultado:
        print(str(user.User.id) + " " + user.User.user_name + ", tipo: " + user.User.userType.utype_name)