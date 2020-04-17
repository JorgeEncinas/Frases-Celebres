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

import argparse #1 punto
import csv #puede omitirse gracias a frases.py
import frases
import Levenshtein #¿Se usará?
import time

# 7 pts

def filtrado_frases(listado,frase,limite):      # Funcion de filtrado de frases
        lista=frases.levDistance(listado,frase,limite)
        return lista

# 5 pts

def despliega_frases(lista):     # despliegue() que despliega lista de frases filtradas
    #lista_titulos = []
    dfrv = dict()
    if len(lista) > 0:
        typing("Pyshtein: Hemos encontrado una coincidencia en nuestra base de datos !(•̀ᴗ•́)و ̑̑ ")
        for elemento in lista:
            #frase_temp = "\"",elemento[1],"\""," - ", elemento[2], ":",elemento[0]
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
    for letra in frase:
        print(letra, end="", flush = True)
        time.sleep(0.05)
    print("")

# EXTRA ---- LEAN EL 3 ----------------------------------------------------------

# 2 pts ------ 

def frases_mf( dfrv ):  # agregar una funcion que obtenga frases célebres de la misma fuente (si existen)
    dict_tf = frases.findme(dfrv, archivo) # y cree una nueva lista, que pueda ser desplegada por la función de despliegue()
    typing("Pyshtein: Veamos, qué otras frases de los títulos hay (‘•̀ ▽ •́ )✎") 
    for titulo, lista_frases in dict_tf.items():
        if len(lista_frases) > 0:
            typing("Del título {}, he encontrado: ".format(titulo))
            for frase in lista_frases:
                typing("\"{}\"".format(frase))
    typing("\nPyshtein: Ya no hay más ✧*｡٩(ˊᗜˋ*)و✧*｡")          

# 3 pts ---> En lugar de usar funciones, usar objetos (clases y métodos)




def main( archivo, frase, limite ): #1 punto
    typing("Pyshtein: ¡Hola, soy Pyshtein!")
    if limite > 1:
        limite = limite/100
    elif limite < 0:
        typing("Pyshtein: ¿Qué crees que haces? Ese número no es un porcentaje de algún tipo (　ﾟДﾟ)＜!!")
    if len(frase) < 1:
        typing("Pyshtein: ¡No pusiste una frase! ( ‾᷅⚰‾᷄ ) \nInténtalo de nuevo ₍₍ ◝(•̀ㅂ•́)◟ ⁾⁾")
    else:
        listaso=filtrado_frases(archivo,frase,limite)               #2 pts por llamarla
        dfrv = despliega_frases(listaso)                   #2 pt por llamarla
        if len(dfrv) > 0:
            frases_mf( dfrv )
        

if __name__ == "__main__":      #1 punto
    parse =argparse.ArgumentParser()
    parse.add_argument("-a","--archivo",dest="archivo",required=False,default="frases.csv")     #2 pts
    parse.add_argument("-f", "--frase", dest="frase", required=False, default="")               #2 pts
    parse.add_argument("-l", "--limite", dest="limite", type=float, required = False, default = 0.50)                             #2 pts
    args = parse.parse_args()
    archivo = args.archivo
    frase = args.frase
    limite = args.limite
    main( archivo, frase, limite )
