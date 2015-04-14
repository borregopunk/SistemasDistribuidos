#############################################################################
##@Autor: Pablo Borrego Gutierrez                                          ##
##@Ejercicio: Seminario 3                                                  ##
#############################################################################

#<-------># Imports #<------->#
import twitter
import io
import json

#<-------># Funciones #<------->#
#Funcion para loguearse en Twitter
def oauth_login():
    CONSUMER_KEY = '8EbPEo71Df4fQmQLV1JMzWICE'
    CONSUMER_SECRET = '3mCbtdwrLkg7QsbRnObuc3KpsyOSTrbHBVVj0Qd0xhlJemJ9KK'
    OAUTH_TOKEN = '3108944081-frZqMtoyw1kkv0QDr5Jv4uPaS7InE2hJmwDtiqC'
    OAUTH_TOKEN_SECRET = 'YcAnEwVmaO1bzsYxIA6mRgVGT5VniOFaGbJfQpzX83wf3'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Funcion para guardar un JSON en un fichero
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Funcion que te devuelve una lista de coordenadas
def buscarTweets(palabra_a_buscar):
	miUsuario = oauth_login()
	resultado_busqueda = miUsuario.search.tweets(q=palabra_a_buscar, count=1000, geocode='40.00,-3.7,350mi')
	save_json('busqueda', resultado_busqueda)
	contenido = json.loads(open('busqueda.json').read())
	lista_coordenadas = []

	for tweet in contenido["statuses"]:
		if tweet["coordinates"] is not None: 
			lista_coordenadas+="(",(tweet["geo"]["coordinates"][0],tweet["geo"]["coordinates"][1]),")"

	for tweet in lista_coordenadas: 
		lista_coordenadas.remove("(")
		lista_coordenadas.remove(")")

	return lista_coordenadas