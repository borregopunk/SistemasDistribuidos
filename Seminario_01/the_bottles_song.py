#@Autor: Pablo Borrego Gutierrez

#Declaración de funciones
def fun_Song(numero_botellas):
    while(numero_botellas > 0):
        print numero_botellas , "bottles of beer on the wall, " , numero_botellas , "bottles of beer."
        numero_botellas -= 1
        print "Take one down, pass it around, " , numero_botellas , "bottles of beer on the wall.\n"

#main
fun_Song(99)
