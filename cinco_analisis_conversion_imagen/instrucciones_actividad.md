# **Analisis de conversion de imagen**

### Instrucción.

Realizar la conversion de imagen utilizando una matriz de "1"s:

| 1 | 1 | 1 |
|---|---|---|
| 1 | 1 | 1 |
| 1 | 1 | 1 |

Con la siguiente imagen:

| 006 | 018 | 021 | 180 | 018 |
|-----|-----|-----|-----|-----|
| 060 | 012 | 013 | 020 | 021 |
| 070 | 071 | 068 | 041 | 013 |
| 019 | 016 | 117 | 160 | 160 |
| 021 | 211 | 216 | 217 | 130 |

**Metodo:**

La matriz de "1"s se colocara en el centro de cada pixel de la imagen, sus alrededores conformaran parte de las operaciones que afectaran al centro que sera la posicion origen **(Los valores que se encuentran por fuera de la matriz afectada cambiaran de valor a "0", para no afectar el tamaño de la imagen)**, cada valor en la matriz origen se multiplcara con el valor encontrado en la matriz de conversion, obteniendo algunos resultados que posteriormente seran sumados para posteriormente obtener un nuevo resultado para una nueva matriz **(El nuevo resultado se encontrara en la posicion origen)**

**Ejemplo**

Si la matriz de conversion anterior se coloca en el centro de la posicion X = 0, Y = 0, encontraremos que los valores "006" **(Valor origen)**, 018, 060 y 012 seran los valores afectados para la posicion origen, habiendolos identificado se prosigue a realizar las multiplicaciones y las sumas:

1. 006 ==> (6 x 1) + (18 x 1) + (60 x 1) + (12 x 1) ==> 096

El resultado sera el nuevo valor de la nueva matriz para la misma posicion origen **(X = 0, Y = 0)**, teniendolo continuaremos con la siguiente posición y con el resto de la linea:


1. 018 ==> 6 X 1 + 18 X 1 + 21 X 1 + 60 X 1 + 12 X 1 + 13 X 1 ==> 130
1. 021 ==> 18 X 1 + 21 X 1 + 180 X 1 + 12 X 1 + 13 X 1 + 20 X 1 ==> 255
1. 180 ==> 21 X 1 + 180 X 1 + 18 X 1 + 13 X 1 + 20 X 1 + 21 X 1 ==> 255
1. 018 ==> 180 X 1 + 18 X 1 + 20 X 1 + 21 X 1 ==> 239

La matriz de conversion se seguira moviendo a traves de las posicion que se iran modificando, yendo por columnas hasta terminar y continuar con la proxima fila.

**Resto de Operaciones**

1. 060 ==> 6 + 18 + 60 + 12 + 70 + 71 ==> 237
1. 012 ==> 6 + 18 + 21 + 60 + 12 + 13 + 70 + 71 + 68 ==> 255
1. 013 ==> 18 + 21 + 180 + 12 + 13 + 20 + 71 + 68 + 41 ==> 255
1. 020 ==> 21 + 180 + 18 + 13 + 20 + 21 + 68 + 41 + 13 ==> 255
1. 021 ==> 180 + 18 + 20 + 21 + 41 + 13 ==> 255

1. 070 ==> 60 + 12 + 70 + 71 + 19 + 16 ==> 248
1. 071 ==> 60 + 12 + 13 + 70 + 71 + 68 + 19 + 16 + 117 ==> 255
1. 068 ==> 12 + 13 + 20 + 71 + 68 + 41 + 16 + 117 + 160 ==> 255
1. 041 ==> 13 + 20 + 21 + 68 + 41 + 13 + 117 + 160 + 160 ==> 255
1. 013 ==> 20 + 21 + 41 + 13 + 160 + 160 ==> 255

1. 019 ==> 70 + 71 + 19 + 16 + 21 + 211 ==> 255
1. 016 ==> 70 + 71 + 68 + 19 + 16 + 117 + 21 + 211 + 216 ==> 255
1. 117 ==> 71 + 68 + 41 + 16 + 117 + 160 + 211 + 216 + 217 ==> 255
1. 160 ==> 68 + 41 + 13 + 117 + 160 + 160 + 216 + 217 + 130 ==> 255
1. 160 ==> 41 + 13 + 160 + 160 + 217 + 130 ==> 255

1. 021 ==> 19 + 16 + 21 + 211 ==> 255
1. 211 ==> 19 + 16 + 117 + 21 + 211 + 216 ==> 255
1. 216 ==> 16 + 117 + 160 + 211 + 216 + 217 ==> 255
1. 217 ==> 117 + 160 + 160 + 216 + 217 + 130 ==> 255
1. 130 ==> 160 + 160 + 217 + 130 ==> 255

**Nueva Matriz**

| 096 | 130 | 255 | 255 | 239 |
|-----|-----|-----|-----|-----|
| 237 | 255 | 255 | 255 | 255 |
| 248 | 255 | 255 | 255 | 255 |
| 255 | 255 | 255 | 255 | 255 |
| 255 | 255 | 255 | 255 | 255 |

**Resultados con otra matriz de conversion**

| -1 | 0 | 1 |
|----|---|---|
| -2 | 0 | 2 |
| -1 | 0 | 1 |

**Nueva Matriz con Nuevo Resultado**

| 48 | -17 | 332 | 2 | -380 |
|----|-----|-----|---|------|
| -196 | -81 | 148 | -42 | 73 |
| -219 | 47 | 92 | -59 | 207 |
| -129 | 389 | 264 | -55 | 463 |
| -59 | 391 | 294 | 0 | -537 |

## **Dato importante**

Como los valores dentro de la matriz son valores que define algun color, el rango debe ser entre 0 y 255, por lo que valores mayores o menos a estos se deben de convertir a numeros positivos del rango. Por lo que, numero mayores a 255 **se deben convertir a un maximo de 255**, mientras que los menores **se deben convertir a un minimo de 0**
