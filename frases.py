import csv
import Levenshtein


def carga_csv(archivo):
    lista = []
    try:
        with open(archivo,'r') as fh:
            lector_csv = csv.reader(fh)
            for linea in lector_csv:
                lista.append(linea)
    except IOError as e:
        print(e)
    return lista




archivo = "frases.csv"


listado = carga_csv(archivo)
#texto   = "salva una vida, salva al mundo"
texto   = "Todos esos momentos se perderán en el tiempo"
max_dist = 0
print("Frase a buscar: %s" % texto)
for linea in listado:
    pelicula = linea[1]
    frase = linea[0]
    distancia = Levenshtein.ratio(frase, texto)
    if distancia > 0.50:
        print(distancia, frase, pelicula)

