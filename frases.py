import csv
import Levenshtein


def carga_csv(archivo):
    lista = []
    try:
        with open(archivo,'r', encoding="UTF-8") as fh:
            lector_csv = csv.reader(fh)
            for linea in lector_csv:
                lista.append(linea)
    except IOError as e:
        print(e)
    return lista

def levDistance(archivo, texto, max_dist):
    listado = carga_csv(archivo)
    lista=[]
    print("Frase a buscar: %s" % texto)
    for linea in listado:
        pelicula = linea[1]
        frase = linea[0]
        distancia = Levenshtein.ratio(frase, texto)
        if distancia >= max_dist:
            elemento=(distancia, frase, pelicula)
            lista.append(elemento)
    return lista




