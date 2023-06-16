"""Servicio Datasource para Usuarios"""
from sqlalchemy import select, update
from entities.groups import Group
from lib.dbconnection import db

class GroupsDS():
    
    def listaGrupos(self):
        statement = select(Group)
        results = db.session.execute(statement).all()
        return results
    
    def obtenerGrupo(self, uid):
        statement = select(Group).where(Group.idgroup == uid)
        resultado = db.session.execute(statement).scalar_one()
        return resultado
    
    def guardarGrupo(self, grupo):
        
        if(grupo.idgroup == None):
            db.session.add(grupo)
        else:
            db.session.merge(grupo)
        db.session.commit()    
        return grupo
        
    
    