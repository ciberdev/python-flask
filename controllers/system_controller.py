from sqlalchemy import select
from flask import redirect, render_template, session, request
from flask.helpers import url_for
from entities.users import User
from lib.dbconnection import db

def login():
    error = None
    if request.method == 'POST':
        statement = select(User).where(User.user_name == request.form['username'] and User.password == request.form['password'])
        dbuser = db.session.execute(statement).first()

        if not dbuser == None:
            session['loggedIn'] = True
            session['logged_user'] = dbuser
            return redirect(url_for('bpsystem.inicio'))
        else:
            error = 'Credenciales inválidas.  Por favor intente de nuevo'
            
    datos = { 'title': 'Bienvenido a nuestro sitio oficial', 'usuario': 'Venancio'}
    return render_template('login.html', data=datos, error=error)

def inicio():
    datos = {"title": "Página Principal", "message":"Bienvenido a nuestro sitio"}
    if (session.get('loggedIn', False)):
        return render_template('inicio.html', datos=datos)
    return render_template('login.html')   

def logout():
    session.clear()
    return redirect( url_for('bpsystem.login'))