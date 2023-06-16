import datetime
from flask import redirect, render_template, session, request
from flask.helpers import url_for
from entities.users import User
from lib.dbconnection import db
from repositories.usersds import UsersDS

def list():
    servicioDB = UsersDS()
    if request.method == 'POST':
        if(request.form['operation']=='NUEVO'):
            usuario = User(user_name="", password="", first_name="", last_name="", email_address="")
            session['object_user'] = usuario
            return redirect(url_for('bpusers.datos_usuario')) 
            
        if(request.form['operation']=='MODIFICAR'):
            resultado = servicioDB.obtenerUsuario(request.form['selected_user'])
            session['object_user'] = resultado.User
            if(resultado != None):
                return redirect(url_for('bpusers.datos_usuario')) 
            #render_template('datos_usuario.html', usuario=resultado.User)

        if(request.form['operation']=='ELIMINAR'):
            pass
        
    datos = {"title": "Modulo de Usuarios", "message":"Bienvenido a nuestro sitio"}
    if (session.get('loggedIn', False)):
        # Acá debemos obtener los datos de los usuarios, previo a invocar a la plantilla.
        users = servicioDB.listaUsuarios()
        
        return render_template('users.html', datos=datos, users=users)
    return render_template('login.html')     

def datos_usuario():
    usuario = session['object_user']
    if request.method == 'POST':
        form = request.form
        usuario = User(id=None, user_name=form['user_name'], email_address=form['email_address'],
                    password=form['password'], first_name=form['first_name'], last_name=form['last_name'], 
                    created=datetime.datetime.now(),
                    idtype=1)
        db.session.add(usuario)
        db.session.commit()

    return render_template('datos_usuario.html', usuario=usuario) 

def eliminar_usuario():
    pass