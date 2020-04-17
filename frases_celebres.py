#!/usr/bin/python3
# Integrantes del equipo:
#   Alcaraz Biebrich Manuel Alejandro
#   Encinas Alegre Jorge Carlos
#   Romero Andrade Paula Cristina
# Fecha: 8 de Abril de 2020
#  
#   ./frases_celebres.py -a frases.csv -f "salva una vida, salva al mundo" -l 80
#   -a --archivo  Archivo con las frases célebres 
#   -f --frase    Frase a buscar:
#   -l --limite   Límite menor para resultados iguales o mayores a la tasa/radio de similitud proporcionado. 
#                 Es un porcentaje.

import argparse
import frases
import time

def filtrado_frases(listado,frase,limite):
    ''' Recibe el archivo de frases, la frase, y el porcentaje, y llama a frases.py para ejecutar la funcion. \
    Regresa la lista de frases relevantes en tuplas de tres elementos.'''
    lista=frases.levDistance(listado,frase,limite)
    return lista

def despliega_frases(lista):
    ''' Despliega la lista de frases que tienen relación con la frase introducida. \
    Regresa un diccionario con ellas para evitar repetirlas al listar otras frases de la misma película.'''
    dfrv = dict()
    if len(lista) > 0:
        typing("Pyshtein: Hemos encontrado una coincidencia en nuestra base de datos !(•̀ᴗ•́)و ̑̑ ")
        for elemento in lista:
            frase_temp = "Con coincidencia de {}% -> \" {} \" - {}".format(round(elemento[0]*100, 2), elemento[1], elemento[2])
            typing(frase_temp)
            if elemento[2] not in dfrv.keys():
                dfrv[elemento[2]] = [elemento[1]]
            else:
                dfrv[elemento[2]].append(elemento[1])
    else:
        typing("Pyshtein: Lo sentimos, no hemos encontrado nada ໒( •́ ∧ •̀ )७ \n")
    return dfrv

def typing( frase ):
    ''' Pyshtein: ¡Con esta función simulo hablar lentamente!. Recibo la frase a decir y la escribo tomando pausas.'''
    for letra in frase:
        print(letra, end="", flush = True)
        time.sleep(0.05)
    print("")

def frases_mf( dfrv ):
    ''' Recibe un diccionario de frases que ya se imprimieron. \
    Imprime las demás frases de los títulos que tuvieron coincidencia. '''
    dict_tf = frases.findme(dfrv, archivo)
    typing("Pyshtein: Veamos, qué otras frases de los títulos hay (‘•̀ ▽ •́ )✎") 
    for titulo, lista_frases in dict_tf.items():
        if len(lista_frases) > 0:
            typing("Del título {}, he encontrado: ".format(titulo))
            for frase in lista_frases:
                typing("\"{}\"".format(frase))
    typing("\nPyshtein: Ya no hay más ✧*｡٩(ˊᗜˋ*)و✧*｡")          

# 3 pts ---> En lugar de usar funciones, usar objetos (clases y métodos)

def main( archivo, frase, limite ):
    typing("Pyshtein: ¡Hola, soy Pyshtein!")
    if limite > 1:
        limite = limite/100
        if limite > 1:
            typing("Pyshtein: Pusiste un número muy grande! (　ﾟДﾟ)＜!! \nPyshtein: Pondré el límite en 50% ٩(ˊᗜˋ*)و")
            limite = 0.50
    elif limite < 0:
        typing("Pyshtein: ¿Qué crees que haces? Ese número no es un porcentaje de algún tipo (　ﾟДﾟ)＜!!")
    if len(frase) < 1:
        typing("Pyshtein: ¡No pusiste una frase! ( ‾᷅⚰‾᷄ ) \nPyshtein: Inténtalo de nuevo ₍₍ ◝(•̀ㅂ•́)◟ ⁾⁾")
    else:
        typing("Porcentaje mínimo de búsqueda: {}%".format(round(limite*100, 2)))
        listaso=filtrado_frases(archivo,frase,limite)
        dfrv = despliega_frases(listaso)
        if len(dfrv) > 0:
            frases_mf( dfrv )
        
if __name__ == "__main__":
    parse =argparse.ArgumentParser()
    parse.add_argument("-a","--archivo",dest="archivo",required=False,default="frases.csv")
    parse.add_argument("-f", "--frase", dest="frase", required=False, default="")
    parse.add_argument("-l", "--limite", dest="limite", type=float, required = False, default = 0.50)
    args = parse.parse_args()
    archivo = args.archivo
    frase = args.frase
    limite = args.limite
    main( archivo, frase, limite )
