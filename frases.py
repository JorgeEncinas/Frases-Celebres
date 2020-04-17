import csv
import Levenshtein
import frases_celebres


def carga_csv(archivo):
    '''Recibe un archivo csv y regresa una lista con cada una de sus líneas.'''
    lista = []
    try:
        with open(archivo,'r', encoding="UTF-8") as fh:
            lector_csv = csv.reader(fh)
            for linea in lector_csv:
                lista.append(linea)
    except IOError as e:
        print(e)
    return lista

def normalize(s):
    '''Quita acentos, puntos, comas, signos, y regresa.'''
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        (",", ""),
        (".", ""),
        ("…", ""),
        ("¿", ""),
        ("?", ""),
        ("!", ""),
        ("¡", ""),
        ("«", ""),
        ("»", ""),
        (";", ""),
        (":", ""),
        ("—", ""),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s    

def findme( dfrv, archivo ):
    '''Recibe un diccionario titulo:[lista_de_frases] y un archivo. regresa un diccionario del mismo tipo, \
    pero con aquellas frases que no se hayan impreso.'''
    dict_tf = dict()
    for titulo in dfrv.keys():
        dict_tf[titulo] = []
    listado = carga_csv(archivo)
    for linea in listado:
        if linea[1] in dfrv.keys():
            if linea[0] not in dfrv[linea[1]]:
                dict_tf[linea[1]].append(linea[0])
    return dict_tf

def levDistance(archivo, texto, max_dist):
    '''Calcula la distancia Levenshtein y a partir de ella regresa una lista con sólo aquellas frases que \
    cumplan con la distancia límite establecida.'''
    listado = carga_csv(archivo)
    lista=[]
    frases_celebres.typing("Frase a buscar: \"%s\"  (￣∇￣*)ゞ" % texto)
    for linea in listado:
        pelicula = linea[1]
        frase = linea[0]
        distancia = Levenshtein.ratio(normalize(frase.lower()), normalize(texto.lower()))
        if distancia >= max_dist:
            elemento=(distancia, frase, pelicula)
            lista.append(elemento)
    return lista




