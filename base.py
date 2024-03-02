import sqlite3

# Conectar a la base de datos (creará la base de datos si no existe)
conn = sqlite3.connect('base_proyectos.db')

# Crear un cursor
cursor = conn.cursor()

# Definir los comandos SQL para crear las tablas
crear_tabla_usuarios = '''
CREATE TABLE IF NOT EXISTS Usuarios (
    id_usuario INTEGER PRIMARY KEY,
    nombre_usuario TEXT NOT NULL,
    correo_usuario TEXT NOT NULL,
    perfil_usuario TEXT
)
'''

crear_tabla_proyectos = '''
CREATE TABLE IF NOT EXISTS Proyectos (
    id_proyecto INTEGER PRIMARY KEY,
    id_usuario INTEGER,
    nombre_proyecto TEXT NOT NULL,
    detalles_proyecto TEXT,
    estado_proyecto TEXT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
)
'''

crear_tabla_tareas = '''
CREATE TABLE IF NOT EXISTS Tareas (
    id_tarea INTEGER PRIMARY KEY,
    id_usuario INTEGER,
    id_proyecto INTEGER,
    nombre_tarea TEXT NOT NULL,
    estado_tarea TEXT,
    detalles_tarea TEXT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_proyecto) REFERENCES Proyectos(id_proyecto)
)
'''

# Ejecutar los comandos SQL para crear las tablas
cursor.execute(crear_tabla_usuarios)
cursor.execute(crear_tabla_proyectos)
cursor.execute(crear_tabla_tareas)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()