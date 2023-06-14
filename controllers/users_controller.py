from flask import redirect, render_template, session
from lib.dbconnection import db
from repositories.usersds import UsersDS

def list():
    datos = {"title": "Modulo de Usuarios", "message":"Bienvenido a nuestro sitio"}
    servicioDB = UsersDS()
    if (session.get('loggedIn', False)):
        # Acá debemos obtener los datos de los usuarios, previo a invocar a la plantilla.
        users = servicioDB.listaUsuarios()
        
        return render_template('users.html', datos=datos, users=users)
    return render_template('login.html')     