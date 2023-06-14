"""Servicio Datasource para Usuarios"""
from sqlalchemy import select
from entities.users import User
from lib.dbconnection import db

class UsersDS():
    
    def listaUsuarios(self):
        statement = select(User)
        results = db.session.execute(statement).all()
        print(results)
        return results