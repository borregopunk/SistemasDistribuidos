#############################################################################
##@Autor: Pablo Borrego Gutierrez                                          ##
##@Ejercicio: Seminario 3                                                  ##
#############################################################################

#<-------># Imports #<------->#
import twitter
import io
import json
from flask import request
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
from funciones.Funciones import oauth_login
from funciones.Funciones import save_json
from funciones.Funciones import buscarTweets

#<-------># Variables #<------->#
app = Flask(__name__)
GoogleMaps(app)

#Funcion para crear un mapa
@app.route("/buscar", methods=['POST'])
def buscar():
	termino = request.form['text'] 
	lista_coordenadas = buscarTweets(termino)
	
	mymap = Map(
	    identifier="view-side",
	    lat=40.00, 
	    lng=-3.7,
	    markers=lista_coordenadas,
	    zoom = 6,
		style="height:550px;width:1200px;margin:0;"
	) 
	return render_template('template2.html', mymap=mymap)

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()
