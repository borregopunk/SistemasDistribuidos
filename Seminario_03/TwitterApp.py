#############################################################################
##@Autor: Pablo Borrego Gutierrez                                          ##
##@Ejercicio: Seminario 3                                                  ##
#############################################################################

#<-------># Imports #<------->#
import twitter
import io
import json
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
from funciones.Funciones import oauth_login
from funciones.Funciones import save_json

#<-------># Autenticacion #<------->#
miUsuario = oauth_login()

#<-------># Variables #<------->#
app = Flask(__name__)
GoogleMaps(app)

#<-------># App #<------->#
palabra_a_buscar = raw_input('Introduzca la palabra para buscar: ')
numero_de_tweets = int(raw_input('Introduzca el numero de tweets que desee recibir: '))
resultado_busqueda = miUsuario.search.tweets(q=palabra_a_buscar, count=numero_de_tweets, geocode='40.00,-3.7,350mi')
save_json('busqueda', resultado_busqueda)
contenido = json.loads(open('busqueda.json').read())
lista_coordenadas = []

for item in contenido["statuses"]:
	if item["coordinates"] is not None: 
		lista_coordenadas+="(",(item["geo"]["coordinates"][0],item["geo"]["coordinates"][1]),")"

for marker in lista_coordenadas: 
	lista_coordenadas.remove("(")
	lista_coordenadas.remove(")")

#Funcion para crear un mapa
@app.route("/")
def mapview():
	mymap = Map(
	    identifier="view-side",
	    lat=40.00, 
	    lng=-3.7,
	    markers=lista_coordenadas,
	    style="height:550px;width:1200px;margin:0;",
	    zoom = 6
	) 
	return render_template('template2.html', mymap=mymap)

if __name__ == "__main__":
	app.run()
