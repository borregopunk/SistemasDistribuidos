#############################################################################
##@Autor: Pablo Borrego Gutierrez                                          ##
##@Ejercicio: Seminario 2                                                  ##
##@Titulo: Numero maximo de palabras encadenadas de una lista de palabras  ##
#############################################################################

#<-------># DECLARACION DE FUNCIONES #<------->#
    
#Funcion que recibe una URL de un fichero y devuelve un string
#con la primera linea del fichero
def abrirArchivo(URLfichero):
    fichero = open(URLfichero, "r")
    contenido_fichero = fichero.readlines()
    return contenido_fichero

#Funcion que recibe un string y lo recorre, insertando en cada posicion 
#de una lista las palabras que encuentra. Luego devuelve la lista
def cargarLista(cursor):
    palabras = []
    for i in cursor:
        for palabra in i.split(' '):
               if(palabra != "\n"):
                palabras.append(palabra)
    return palabras

#Funcion que recibe dos palabras y devuelve si la primera letra 
#de la primera y la ultima letra de la otra son iguales
def comprobarLetras(p1, p2):
    return p1[len(p1)-1] == p2[0]

#Funcion que devuelve una lista de palabras encadenadas en funcion de una lista
#y una palabra que recibe como parametro
def crearEncadenadas(elementos_actuales, palabra_temporal, pokedex, lista_temporal):
    i = 0
    while i < elementos_actuales:
        if(comprobarLetras(palabra_temporal, pokedex[i])):
            lista_temporal.append(pokedex[i])
            palabra_temporal = pokedex[i]
            pokedex.pop(i)
            elementos_actuales-=1
            i=-1
        i+=1
    return lista_temporal

def devolverMayorLista(lista):
    mayor = 0
    for i in range(0, len(lista)):
        if(len(lista[i])>mayor):
            mayor = i
    return lista[mayor]

#<-------># PROGRAMA #<------->#

#Carga de los archivos necesarios
contenido_fichero = abrirArchivo("pokemon")
pokedex = cargarLista(contenido_fichero)

#Declaracion de variables globales
lista_completa = []
lista_temporal = []
numero_total_pokemon = len(pokedex)

for j in range(0, numero_total_pokemon):
    pokedex = cargarLista(contenido_fichero)
    elementos_actuales = len(pokedex)-1
    palabra_temporal = pokedex[j]
    lista_temporal.append(pokedex[j])
    pokedex.pop(j)
    lista_completa.append(crearEncadenadas(elementos_actuales, palabra_temporal, pokedex, lista_temporal))
    lista_temporal = []

print devolverMayorLista(lista_completa)