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
