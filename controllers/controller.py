
from sqlalchemy import select
from entities import User
import datetime

class UsersController():
    
    def crearUsuario(self, session):
        vuser_name = input("Ingrese un usuario: ")
        vpassword = input("Ingrese contraseña:")
        vemail_address = input("Ingrese correo-e:")
        vlast_name = input("Ingrese apellidos:")
        vfirst_name = input("Ingrese nombres:")

        usuario = User(id=None, user_name=vuser_name, email_address=vemail_address,
                    password=vpassword, first_name=vfirst_name, last_name=vlast_name, created=datetime.datetime.now(),
                    idtype=1)    
        session.add(usuario)
        session.commit()
        
    def mostrarUsuarios(self, session):
        statement = select(User)
        resultado = session.execute(statement).all()
        
        print("Listado de usuarios en la BD:")
        for user in resultado:
            print(str(user.User.id) + " " + user.User.user_name + ", tipo: " + user.User.userType.utype_name)