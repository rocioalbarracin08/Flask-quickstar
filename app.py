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

###--------------------CONEXION A BASE DE DATOS----------------------------------

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



