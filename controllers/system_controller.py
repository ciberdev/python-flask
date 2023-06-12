from flask import redirect, render_template, session, request
from flask.helpers import url_for

def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['loggedIn'] = True
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
