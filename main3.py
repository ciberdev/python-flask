from flask import Flask, render_template, request, redirect, session
from flask.helpers import url_for
from flask_bootstrap import Bootstrap5
from flask_session import Session

app=Flask(__name__)

# Configuramos la libreria de estilos
Bootstrap5(app)

# Configuramos la app para el uso de sesiones.
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/inicio')
def inicio():    
    datos = {"title": "Página Principal", "message":"Bienvenido a nuestro sitio"}
    if (session.get('loggedIn', True)):
        return render_template('inicio.html', datos=datos)
    else:
        return redirect(url_for('root'))        
@app.route('/', methods=['GET', 'POST'])
def root():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['loggedIn'] = True
            return redirect(url_for('inicio'))
        else:
            error = 'Credenciales inválidas.  Por favor intente de nuevo'
            
    datos = { 'title': 'Bienvenido a nuestro sitio oficial', 'usuario': 'Venancio'}
    return render_template('login.html', data=datos, error=error)

if __name__ == '__main__':
    app.run(debug=True)