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

# 7 pts

def filtrado_frases(listado,frase,limite):      # Funcion de filtrado de frases
        lista=frases.levDistance(listado,frase,limite)
        return lista


# 5 pts

def despliega_frases(lista):     # despliegue() que despliega lista de frases filtradas
    for elemento in lista:
        print("\"",elemento[1],"\""," - ", elemento[2], ":",elemento[0])

# EXTRA ---- LEAN EL 3 ----------------------------------------------------------

# 2 pts ------ 

def frases_misma_fuente():  # agregar una funcion que obtenga frases célebres de la misma fuente (si existen)
    return 1                # y cree una nueva lista, que pueda ser desplegada por la función de despliegue()

# 3 pts ---> En lugar de usar funciones, usar objetos (clases y métodos)




def main( archivo, frase, limite ): #1 punto
    if limite > 1:
        limite = limite/100
    listaso=filtrado_frases(archivo,frase,limite)               #2 pts por llamarla
    despliega_frases(listaso)                                   #2 pt por llamarla

if __name__ == "__main__":      #1 punto
    parse =argparse.ArgumentParser()
    parse.add_argument("-a","--archivo",dest="archivo",required=False,default="frases.csv")     #2 pts
    parse.add_argument("-f", "--frase", dest="frase")                                           #2 pts
    parse.add_argument("-l", "--limite", dest="limite", type=float, required = False, default = 0.50)                             #2 pts
    args = parse.parse_args()
    archivo = args.archivo
    frase = args.frase
    limite = args.limite
    main( archivo, frase, limite )
