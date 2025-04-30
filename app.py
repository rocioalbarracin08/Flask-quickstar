from flask import Flask, url_for
import sqlite3

app = Flask(__name__)

db = None

#@app.route("/") Solo puede haber un principal
#def principal():
#    return "<p>Hola Rocío. Exitos para este año! :)</p>"

@app.route("/") #Devuelve lo que ve en el navegador
def principal():
    url_consulta = url_for("consultaxn", nombre='Rocío') #usamos el def "consultaxn" y con una coma ponemos el parametro que recibe
    url_dado = url_for("dado", caras=6) # Variables que guardan...
    url_logo = url_for("static", filename = "static/imagen.png")
    return f"""
        <a href="{url_consulta}">Pregunta por nombre</a>
        <br>
        <a href="{url_for("respuesta")}">Respuesta</a>
        <br>
        <a href="{url_logo}">Logo</a>
        <br>
        <a href="{url_dado}">Tirar_dado</a>
    """

#<a href='/consultaxn'>preguntaxn</a>  (1)
#<a href="{url_consulta}">Pregunta</a>  (2)
#--> 2 formas diferentes que hacen lo mismo, la opción(2) es mas recomendada CREA LA URL CON "url_for()"

#<a href="{url_for("respuesta")}">Respuesta</a> -> Este va al def de "respuesta"

#si se presiona ... se muestra ...
@app.route("/pregunta")
def consulta():
    return "<p>como amaneciste?!</p>"
#si se presiona ... se muestra ...
@app.route("/respuesta")
def respuesta():
    return "<p>Nos vemos!</p>"


#2 rutas y 2 links
@app.route("/consulta/<string:nombre>")
def consultaxn(nombre):  #con argumento
    return f"<p>¿Cómo estas {nombre}?</p>"

@app.route("/hola")
def saludar():               #sin argumento
    return "<h2> Hola! </h2>"
@app.route("/hola/<string:nombre>") #El argumento nombre se pasa por parámetro
def saludar_con_nombre(nombre):
    return f"<h2> Hola {nombre}! </h2>"

@app.route("/dado/<int:caras>")
def dado(caras):
    from random import randint
    numero = randint (1,caras)
    return f"<p> dado de {caras} caras, salio {numero}! </p>"

@app.route("/suma/<int:n1>/<int:n2>")
def suma(n1,n2):
    suma = n1 +n2
    return f"<p>{n1} mas {n2} da {suma}</p>"

###--------------------CONEXIÒN A BASE DE DATOS----------------------------------

def abrirConexion():
    global db
    db = sqlite3.connect('instance/datos.sqlite')
    db.row_factory = sqlite3.Row
    return db

def cerrarConexion():
    global db
    if db is not None:
        db.close()
        db = None

@app.route("/usuarios") # Para conectarlo en la pag, ponemos "/usuarios"
def obterGente():
    global db
    conexion = abrirConexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios ")
    resultado = cursor.fetchall()
    cerrarConexion()
    fila = [dict(row) for row in resultado]
    return str(fila)

db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)} #Devuelve un diccionario


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def cerrarConexion():
   global db
   db.close()
   db = None


@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone() 
   registros = res["cant"] #Saca el valor usando la clave
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"


#----------Ejercicio----------
'''
1 - Insertar un usuario nuevo (2 parámetros: nombre, mail)
2 - Borre un usuario (1 parámetro: id)
3 - Nombre y mail usuario (1 parámetro: id)
4 - Cambiar el mail (nombre, mail -> con el nombre que coincida)
'''
# 1
@app.route("/insertar/<string:nombre>/<string:mail>")
def insertar_usuario(nombre, mail):
    global db
    abrirConexion() #Tener conexion abierta el minimo tiempo posible
    db.execute("INSERT INTO usuarios(usuario,email) VALUES (?,?);", (nombre, mail))
    db.commit()
    cerrarConexion()
    return f"Hay un nuevo registro con el nombre {nombre} y el mail {mail}"

# 3
@app.route("/mostrar/<int:id>")
def mostrar_usuario(id):
    global db
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT usuario, email FROM usuarios WHERE id = ?", (id,)) #Indicamos con una coma que es una tupla
    res = cursor.fetchone() 
    cerrarConexion()
    return f"nombre: {res['usuario']}, email: {res['email']}"

# 2
@app.route("/borrar/<int:id>")
def borrar_usuario(id):
    global db
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,)) #Indicar siempre dónde hay que borrar, si le pongo solo FROM tabla (borra toda la tabla)
    #res = cursor.fetchone() 
    db.commit()
    cerrarConexion()
    return f"El usuario eliminado tiene el N* de ID: {id}"

# 4
@app.route("/cambio/<string:nombre>/<string:email>")
def cambiar_mail(nombre, email):
    global db
    abrirConexion()

    cerrarConexion()
    return f"El email cambiado es: {res} por el email {email}"