import sqlite3
#creando tabla
conn=sqlite3.connect('baseDeDatos.db')
cursor=conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT,username VARCHAR(50) UNIQUE, nacimiento VARCHAR(10), mail VARCHAR(50) UNIQUE, password VARCHAR(50))')
def saveData(username,nacimiento,email,password):
    cursor.execute ('INSERT INTO usuarios VALUES (NULL,?,?,?,?)',(username,nacimiento,email,password)) 
    conn.commit()
#trae datos para saber si esta disponible
def loginData(username,password):
    cursor.execute('SELECT * FROM usuarios WHERE username=? AND password=?',
    (username,password))
    #datos que trae el cursor
    if cursor.fetchone()is not None: #¡esta el usuario?
       return True
    else:
        return False
        