from flask import Flask, jsonify, request, g
from flask_httpauth import HTTPBasicAuth
import sqlite3

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):

    conn = sqlite3.connect('base_proyectos.db')
    c = conn.cursor()
    
    c.execute('SELECT username, password, perfilusu FROM Usuarios_cr WHERE username = ?', (username,))
    user = c.fetchone()
    
    if user and user[0] == username and user[1] == password:
        g.perfil = user[2]
        return True
    return False

@app.route('/usuarios', methods=['GET'])
@auth.login_required
def get_usuarios():
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Usuarios')
        usuarios = c.fetchall()
        conn.close()
        return jsonify(usuarios)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Usuarios')
        usuarios = c.fetchall()
        conn.close()
        return jsonify(usuarios)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/usuarios/<int:id>', methods=['GET'])
@auth.login_required
def get_usuario(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Usuarios WHERE id_usuario = ?', (id,))
        usuarios = c.fetchall()
        conn.close()
        return jsonify(usuarios)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Usuarios WHERE id_usuario = ?', (id,))
        usuarios = c.fetchall()
        conn.close()
        return jsonify(usuarios)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/usuarios/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_usuario(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('DELETE FROM Usuarios WHERE id_usuario = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario eliminado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/usuarios', methods=['POST'])
@auth.login_required
def add_usuario():
    if g.perfil == 'Gerente':
        nuevo_usuario = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('INSERT INTO Usuarios (nombre_usuario, correo_usuario, perfil_usuario) VALUES (?, ?, ?)',
                  (nuevo_usuario['nombre_usuario'], nuevo_usuario['correo_usuario'], nuevo_usuario['perfil_usuario']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario agregado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/usuarios/<int:id>', methods=['PATCH'])
@auth.login_required
def update_usuario(id):
    if g.perfil == 'Gerente':
        usuario_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Usuarios SET nombre_usuario = ?, correo_usuario = ?, perfil_usuario = ? WHERE id_usuario = ?',
                  (usuario_actualizado['nombre_usuario'], usuario_actualizado['correo_usuario'], usuario_actualizado['perfil_usuario'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario actualizado correctamente'})
    elif g.perfil == 'Desarrollador':
        usuario_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Usuarios SET nombre_usuario = ?, correo_usuario = ?, perfil_usuario = ? WHERE id_usuario = ?',
                  (usuario_actualizado['nombre_usuario'], usuario_actualizado['correo_usuario'], usuario_actualizado['perfil_usuario'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario actualizado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------TABLA PROYECTOS---------------------------

@app.route('/proyectos', methods=['GET'])
@auth.login_required
def get_proyectos():
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Proyectos')
        proyectos = c.fetchall()
        conn.close()
        return jsonify(proyectos)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Proyectos')
        proyectos = c.fetchall()
        conn.close()
        return jsonify(proyectos)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/proyectos/<int:id>', methods=['GET'])
@auth.login_required
def get_proyecto(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Proyectos WHERE id_proyecto = ?', (id,))
        proyectos = c.fetchall()
        conn.close()
        return jsonify(proyectos)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Proyectos WHERE id_proyecto = ?', (id,))
        proyectos = c.fetchall()
        conn.close()
        return jsonify(proyectos)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/proyectos/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_proyecto(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('DELETE FROM Proyectos WHERE id_proyecto = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'proyecto eliminado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/proyectos', methods=['POST'])
@auth.login_required
def add_proyecto():
    if g.perfil == 'Gerente':
        nuevo_proyecto = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('INSERT INTO Proyectos (id_proyecto, id_usuario, nombre_proyecto, detalles_proyecto, estado_proyecto) VALUES (?, ?, ?, ?, ?)', 
                   (nuevo_proyecto['id_proyecto'], nuevo_proyecto['id_usuario'], nuevo_proyecto['nombre_proyecto'], nuevo_proyecto['detalles_proyecto'], nuevo_proyecto['estado_proyecto']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Proyecto agregado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/proyectos/<int:id>', methods=['PATCH'])
@auth.login_required
def update_proyecto(id):
    if g.perfil == 'Gerente':
        proyecto_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Proyectos SET id_usuario = ?, nombre_proyecto = ?, detalles_proyecto = ?, estado_proyecto = ? WHERE id_proyecto = ?', 
                   (proyecto_actualizado['id_usuario'], proyecto_actualizado['nombre_proyecto'], proyecto_actualizado['detalles_proyecto'], proyecto_actualizado['estado_proyecto'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario actualizado correctamente'})
    elif g.perfil == 'Desarrollador':
        proyecto_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Proyectos SET id_usuario = ?, nombre_proyecto = ?, detalles_proyecto = ?, estado_proyecto = ? WHERE id_proyecto = ?', 
                   (proyecto_actualizado['id_usuario'], proyecto_actualizado['nombre_proyecto'], proyecto_actualizado['detalles_proyecto'], proyecto_actualizado['estado_proyecto'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Proyecto actualizado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------TABLA TAREAS---------------------------


@app.route('/tareas', methods=['GET'])
@auth.login_required
def get_tareas():
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Tareas')
        tareas = c.fetchall()
        conn.close()
        return jsonify(tareas)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Tareas')
        tareas = c.fetchall()
        conn.close()
        return jsonify(tareas)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/tareas/<int:id>', methods=['GET'])
@auth.login_required
def get_tarea(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Tareas WHERE id_tarea = ?', (id,))
        tareas = c.fetchall()
        conn.close()
        return jsonify(tareas)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM tareas WHERE id_tarea = ?', (id,))
        tareas = c.fetchall()
        conn.close()
        return jsonify(tareas)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/tareas/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_tarea(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('DELETE FROM Tareas WHERE id_tarea = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'tarea eliminado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/tareas', methods=['POST'])
@auth.login_required
def add_tarea():
    if g.perfil == 'Gerente':
        nueva_tarea = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('INSERT INTO Tareas (id_tarea, id_usuario, id_proyecto, nombre_tarea, estado_tarea, detalles_tarea) VALUES (?, ?, ?, ?, ?, ?)', 
                   (nueva_tarea['id_tarea'], nueva_tarea['id_usuario'], nueva_tarea['id_proyecto'], nueva_tarea['nombre_tarea'], nueva_tarea['estado_tarea'], nueva_tarea['detalles_tarea']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'tarea agregado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/tareas/<int:id>', methods=['PATCH'])
@auth.login_required
def update_tarea(id):
    if g.perfil == 'Gerente':
        tarea_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Tareas SET id_usuario = ?, id_proyecto = ?, nombre_tarea = ?, estado_tarea = ?, detalles_tarea = ? WHERE id_tarea = ?', 
                   (tarea_actualizado['id_usuario'], tarea_actualizado['id_proyecto'], tarea_actualizado['nombre_tarea'], tarea_actualizado['estado_tarea'], tarea_actualizado['detalles_tarea'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario actualizado correctamente'})
    elif g.perfil == 'Desarrollador':
        tarea_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Tareas SET id_usuario = ?, id_proyecto = ?, nombre_tarea = ?, estado_tarea = ?, detalles_tarea = ? WHERE id_tarea = ?', 
                   (tarea_actualizado['id_usuario'], tarea_actualizado['id_proyecto'], tarea_actualizado['nombre_tarea'], tarea_actualizado['estado_tarea'], tarea_actualizado['detalles_tarea'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'tarea actualizado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})


#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------TABLA ESTADOS-----------------------------


@app.route('/estados', methods=['GET'])
@auth.login_required
def get_estados():
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Estados')
        estados = c.fetchall()
        conn.close()
        return jsonify(estados)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Estados')
        estados = c.fetchall()
        conn.close()
        return jsonify(estados)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/estados/<int:id>', methods=['GET'])
@auth.login_required
def get_estado(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Estados WHERE id_estado = ?', (id,))
        estados = c.fetchall()
        conn.close()
        return jsonify(estados)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Estados WHERE id_estado = ?', (id,))
        estados = c.fetchall()
        conn.close()
        return jsonify(estados)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/estados/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_estado(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('DELETE FROM Estados WHERE id_estado = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Estado eliminado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/estados', methods=['POST'])
@auth.login_required
def add_estado():
    if g.perfil == 'Gerente':
        nuevo_estado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('INSERT INTO Estados (id_estado, nombre_estado) VALUES (?, ?)', 
                   (nuevo_estado['id_estado'], nuevo_estado['nombre_estado']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'estado agregado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/estados/<int:id>', methods=['PATCH'])
@auth.login_required
def update_estado(id):
    if g.perfil == 'Gerente':
        estado_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Estados SET id_estado = ?, nombre_estado = ? WHERE id_estado = ?', 
                   (estado_actualizado['id_estado'], estado_actualizado['nombre_estado'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario actualizado correctamente'})
    elif g.perfil == 'Desarrollador':
        estado_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Estados SET id_estado = ?, nombre_estado = ? WHERE id_estado = ?', 
                   (estado_actualizado['id_estado'], estado_actualizado['nombre_estado'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'estado actualizado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})


#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------TABLA HISTORIAL---------------------------

@app.route('/historial', methods=['GET'])
@auth.login_required
def get_historiales():
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Historial')
        historial = c.fetchall()
        conn.close()
        return jsonify(historial)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Historial')
        historial = c.fetchall()
        conn.close()
        return jsonify(historial)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/historial/<int:id>', methods=['GET'])
@auth.login_required
def get_historial(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Historial WHERE id_historial = ?', (id,))
        historial = c.fetchall()
        conn.close()
        return jsonify(historial)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Historial WHERE id_historial = ?', (id,))
        historial = c.fetchall()
        conn.close()
        return jsonify(historial)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/historial/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_historial(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('DELETE FROM Historial WHERE id_historial = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'historial eliminado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/historial', methods=['POST'])
@auth.login_required
def add_historial():
    if g.perfil == 'Gerente':
        nuevo_historial = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('INSERT INTO Historial (id_historial, id_usuario, id_proyecto, id_tarea, nombre_estado, detalles_h) VALUES (?, ?, ?, ?, ?, ?)', 
                   (nuevo_historial['id_historial'], nuevo_historial['id_usuario'], nuevo_historial['id_proyecto'], nuevo_historial['id_tarea'], nuevo_historial['nombre_estado'], nuevo_historial['detalles_h']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'historial agregado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/historial/<int:id>', methods=['PATCH'])
@auth.login_required
def update_historial(id):
    if g.perfil == 'Gerente':
        historial_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Historial SET id_historial = ?, id_usuario = ?, id_proyecto = ?, id_tarea = ?, nombre_estado = ?, detalles_h = ? WHERE id_historial = ?', 
                   (historial_actualizado['id_historial'], historial_actualizado['id_usuario'], historial_actualizado['id_proyecto'], historial_actualizado['id_tarea'], historial_actualizado['nombre_estado'], historial_actualizado['detalles_h'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario actualizado correctamente'})
    elif g.perfil == 'Desarrollador':
        historial_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Historial SET id_historial = ?, id_usuario = ?, id_proyecto = ?, id_tarea = ?, nombre_estado = ?, detalles_h = ? WHERE id_historial = ?', 
                   (historial_actualizado['id_historial'], historial_actualizado['id_usuario'], historial_actualizado['id_proyecto'], historial_actualizado['id_tarea'], historial_actualizado['nombre_estado'], historial_actualizado['detalles_h'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'historial actualizado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------TABLA PERFILES---------------------------
    
@app.route('/perfiles', methods=['GET'])
@auth.login_required
def get_perfiles():
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM perfiles')
        perfiles = c.fetchall()
        conn.close()
        return jsonify(perfiles)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM perfiles')
        perfiles = c.fetchall()
        conn.close()
        return jsonify(perfiles)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/perfiles/<int:id>', methods=['GET'])
@auth.login_required
def get_perfil(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM perfiles WHERE id_perfil = ?', (id,))
        perfiles = c.fetchall()
        conn.close()
        return jsonify(perfiles)
    elif g.perfil == 'Desarrollador':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('SELECT * FROM perfiles WHERE id_perfil = ?', (id,))
        perfiles = c.fetchall()
        conn.close()
        return jsonify(perfiles)
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/perfiles/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_perfil(id):
    if g.perfil == 'Gerente':
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('DELETE FROM perfiles WHERE id_perfil = ?', (id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'perfil eliminado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/perfiles', methods=['POST'])
@auth.login_required
def add_perfil():
    if g.perfil == 'Gerente':
        nuevo_perfil = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('INSERT INTO Perfiles (id_perfil, nombre_perfil) VALUES (?, ?)', 
                   (nuevo_perfil['id_perfil'], nuevo_perfil['nombre_perfil']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'perfil agregado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})

@app.route('/perfiles/<int:id>', methods=['PATCH'])
@auth.login_required
def update_perfil(id):
    if g.perfil == 'Gerente':
        perfil_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Perfiles SET id_perfil = ?, nombre_perfil = ? WHERE id_perfil = ?', 
                   (perfil_actualizado['id_perfil'], perfil_actualizado['nombre_perfil'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Usuario actualizado correctamente'})
    elif g.perfil == 'Desarrollador':
        perfil_actualizado = request.get_json()
        conn = sqlite3.connect('base_proyectos.db')
        c = conn.cursor()
        c.execute('UPDATE Perfiles SET id_perfil = ?, nombre_perfil = ? WHERE id_perfil = ?', 
                   (perfil_actualizado['id_perfil'], perfil_actualizado['nombre_perfil'], id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'perfil actualizado correctamente'})
    else:
        return jsonify({'message': 'Acceso denegado'})





if __name__ == '__main__':
    app.run(debug=True)
