# Programas de Juguete (Canibales y Monjes, Laberinto y Conteo de Islas)

**Resolver los siguientes ejercicios utilizando la misma logica (Poco a poco ir mejorando)**

1. Ejercicio Canibales y Monjes:
    
    De un lado de la isla tenemos el mismo numero de canibales que de monjes **(Por ejemplo 3 de ambos)**, el reto consiste en trasladar a los canibales y a los monjes a una segunda isla a traves de una canoa. **Reglas:** De un lado de la isla no puede haber mas canibales que monjes, de lo contrario se pierde el intento, esto tambien se aplica si por ejemplo en la segunda isla hay un canibal y se viaja a ella con un camnibal y un monje y solo se deja el monje para regresar el canibal, en este caso se pierde tambien el ejercicio, en la canoa pueden viajar 1 o 2 personas, ya sean camibales, monjes o uno de cada uno. **El ejercicio esta resuelto una vez que, todos los canibales y monjes esten al otro lado de la isla.**

2. Laberinto

    Dentro de una matriz se crea una clase de laberinto, donde se debe encontrar la mejor manera de poder llegar desde un punto A hasta un punto B.

3. Conteo de Islas

    Dentro de una matriz se debe encontrar la manera de poder contar cuantas islas hay dentro de esa matriz, por ejemplo, si contamos con la siguiente matriz.

    | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
    |---|---|---|---|---|---|---|---|---|---|
    | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
    | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

    A simple vista podemos diferenciar al conjunto de unos como islas, teniendo un total de 3 islas dentro de la matriz. **Objetivo:** Sin importar el tamaño de la matriz, lograr contar el total de islas dentro de ella