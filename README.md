# Frases Celebres

Instrucciones
Para esta tarea, se necesita escribir un programa que encuentre una frase célebre entre varias y muestre la referencia a la misma. Será necesario instalar un módulo de Python, el cual se encarga de calcular la distancia entre una cadena de texto de otra. Esta librería se llama Levenshtein.

Si utilizan Anaconda para administrar sus instalaciones, en su “Environment” activo, usen este comando para instalarlo:

conda install -c conda-forge python-levenshtein

Si solo usan el paquete PIP para instalar módulos, entonces el comando es:

pip install python-Levenshtein

Ahora, si quieren averiguar un poquito más sobre el cálculo de distancias entre cadenas:

[Cálculo de Distancias - Levenshtein](https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html)

[Wikipedia - Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)

[Wikipedia - Distancia de Levenshtein](https://es.wikipedia.org/wiki/Distancia_de_Levenshtein)

En nuestro programa lo que vamos a hacer es encontrar el radio o tasa de similitud entre dos cadenas de texto, donde una distancia de 0 indica que las cadenas son totalmente diferentes tanto en símbolos (letras), como en posiciones de estas; mientras que entre más se acerque a 1 la distancia, significa que las cadenas no solo comparten las mismas letras, sino también las mismas posiciones.

En el área de archivos de TEAMS se encuentran dos archivos: frases.py y frases.csv. Descárguenlos y ejecuten el programa frases.py, para que vean como calcula las distancias. Esta es la salida de una ejecución:

Frase a buscar: salva una vida, salva al mundo
  0.7352941176470589 ¡Salva a la animadora, salva el mundo!  "Heroes"
  0.821917808219178 Quién salva una vida, salva al mundo entero  "La lista de Schindler"

Pueden recortar la frase a buscar, ya sea intentar con “salva una vida” o “salva al mundo” y ver que las distancias se acortan, lo que es una mala noticia. Intenten también escribir la frase a buscar muy parecida o idéntica a una de las dos frases anteriores y ver que se acercarán a 1 en una oración y a cero en la otra.

Bien, el programa que tienen que realizar, debe aceptar como argumentos el archivo de frases.csv (opcional / por defecto, “frases.csv”) la frase a buscar y el límite del radio o tasa de similitud entre la frase a buscar y las que se encuentran almacenadas (opcional / por defecto 0.50).

Lo que el programa debe mostrar es: la frase para buscar, la(s) frase(s) encontrada(s) y su(s) fuente(s), así como su distancia o radio/tasa de similitud. Muy importante: Solo debe mostrar resultados iguales o mayores a la tasa/radio de similitud proporcionado en el argumento. Ejemplo:

Frase a buscar: salva una vida, salva al mundo
Quién salva una vida, salva al mundo entero   La lista de Schindler     82%

Pueden utilizar la función carga_csv() que se encuentra en el archivo frases.py.



./frases_celebres.py -a frases.csv -f “salva una vida, salva al mundo” -l 80

./frases_celebres.py --archivo frases.csv --frase “salva una vida, salva al mundo” --limite 80

![cr1](/criterios/cr1.PNG)
