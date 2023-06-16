import datetime
from flask import redirect, render_template, session, request
from flask.helpers import url_for
from entities.groups import Group
from lib.dbconnection import db
from repositories.groupsds import GroupsDS

def list():
    servicioDB = GroupsDS()
    if request.method == 'POST':
        if(request.form['operation']=='NUEVO'):
            grupo = Group(group_name="")
            session['object_group'] = grupo
            return redirect(url_for('bpgroups.datos_grupo')) 
            
        if(request.form['operation']=='MODIFICAR'):
            print("Grupo elegido: " + str(request.form['selected_group']))
            resultado = servicioDB.obtenerGrupo(request.form['selected_group'])
            session['object_group'] = resultado
            if(resultado != None):
                return redirect(url_for('bpgroups.datos_grupo')) 

        if(request.form['operation']=='ELIMINAR'):
            pass
        
    datos = {"title": "Modulo de Usuarios", "message":"Bienvenido a nuestro sitio"}
    if (session.get('loggedIn', False)):
        # Acá debemos obtener los datos de los grupos, previo a invocar a la plantilla.
        groups = servicioDB.listaGrupos()
        
        return render_template('groups.html', datos=datos, groups=groups)
    return render_template('login.html')     

def datos_grupo():
    servicioDB = GroupsDS()
    grupo = session['object_group']

    if request.method == 'POST':
        form = request.form
        if(request.form['idgroup'] != 'None'):
            # Recuperamos una referencia al objeto de BD
            grupo = servicioDB.obtenerGrupo(request.form['idgroup'])
            grupo.group_name=form['group_name']
            
        else:
            grupo = Group(group_name=form['group_name'])
        
        grupo=servicioDB.guardarGrupo(grupo)
    
    return render_template('datos_grupo.html', grupo=grupo) 

def eliminar_grupo():
    pass