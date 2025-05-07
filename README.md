# Flask-quickstar
lista en una plantilla 
Java script corre el navegador cuando ya estamos en la pàgina

La plantilla no implica una base de datos

diferencia entre html statics (no se usa mucho ultimamente; se podria hacer un css, una pag "sobre nosotros". En static no hay cambios, solo tiene solo una ruta/una sola página) o html template (tiene for o if, puede ir cambiando; fuera de statics)

Carpetas con nombres especìficos usados por Flask (Flask busca estas carpetas con nombres predefinidos) - ej: "templates", "static"

---------------------------------- CREAR UN ENTORNO VIRTUAL --------------------------------------
1 - Para crear un entorno virtual, desde la carpeta del proyecto usar el comando:
python -m venv .venv
2 - Para activar el entorno virtual, desde la carpeta del proyecto usar el comando:
source .venv/bin/activate
3 - Para instalar el flask (en el entorno virtual, después de activarlo) usar el comando: 
pip install flask
4 - Para verificar si está instalado el flask usar el comando: 
flask --version
(Debería figurar la versión 2.3.2 o más nueva.)
5 - Para abrir el Visual Studio Code con el proyecto:
code .
