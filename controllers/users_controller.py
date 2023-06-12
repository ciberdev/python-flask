from flask import redirect, render_template, session

def list():
    datos = {"title": "Modulo de Usuarios", "message":"Bienvenido a nuestro sitio"}
    if (session.get('loggedIn', False)):
        return render_template('users.html', datos=datos)
    return render_template('login.html')     