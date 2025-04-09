from flask import Flask, url_for

app = Flask(__name__)

#@app.route("/") Solo puede haber un principal
#def principal():
#    return "<p>Hola Rocío. Exitos para este año! :)</p>"

@app.route("/")
def principal():
    return """
        <a href='/pregunta'>pregunta</a>
        <a href='/respuesta'>respuesta</a>
        <a href='/consultaxn'>preguntaxnombre</a>
    """

@app.route("/pregunta")
def pregunta()
