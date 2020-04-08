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
import csv
import Levenshtein #¿Se usará?

# 7 pts

def filtrado_frases():      # Funcion de filtrado de frases
    return 1

# 5 pts

def despliega_frases():     # despliegue() que despliega lista de frases filtradas
    print("Lista de frases")

# EXTRA ---- LEAN EL 3 ----------------------------------------------------------

# 2 pts ------ 

def frases_misma_fuente():  # agregar una funcion que obtenga frases célebres de la misma fuente (si existen)
    return 1                # y cree una nueva lista, que pueda ser desplegada por la función de despliegue()

# 3 pts ---> En lugar de usar funciones, usar objetos (clases y métodos)




def main( archivo, frase, limite ): #1 punto
    filtrado_frases()               #2 pts por llamarla
    despliega_frases()              #2 pt por llamarla
    print("Hola compañeros")

if __name__ == "__main__":      #1 punto
    parse =argparse.ArgumentParser()
    parse.add_argument("-a","--archivo",dest="archivo",required=False,default="frases.csv") #2 pts
    parse.add_argument("-f", "--frase", dest="frase")                                       #2 pts
    parse.add_argument("-l", "--limite", dest="limite", type=int)                           #2 pts
    args = parse.parse_args()
    archivo = args.archivo
    frase = args.frase
    limite = args.limite
    main( archivo, frase, limite )