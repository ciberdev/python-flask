"""Servicio Datasource para Usuarios"""
from sqlalchemy import select
from entities.users import User
from lib.dbconnection import db

class UsersDS():
    
    def listaUsuarios(self):
        statement = select(User)
        results = db.session.execute(statement).all()
        return results
    
    def obtenerUsuario(self, uid):
        statement = select(User).where(User.id == uid)
        resultado = db.session.execute(statement).first()
        return resultado
    
    def guardarUsuario(self, usuario):
        print(usuario.id)
        if(usuario.id == None):
            db.session.add(usuario)
        else:
            #print(dir(db.session))
            db.session.merge(usuario)
        db.session.commit()    
        
    
    