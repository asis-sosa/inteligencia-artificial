# **Pregunta 1 - Convolución a mano (3x3)**

## *Tienes este trozo de imagen en escala de grises (un canal) y este kernel:*

  ┌────
  │   Imagen 5×5                 Kernel 3×3
  │   0  0  1  0  0              1  0 -1
  │   0  1  2  1  0              1  0 -1
  │   1  2  3  2  1              1  0 -1
  │   0  1  2  1  0
  │   0  0  1  0  0
  └────

**Tareas:**

1. Con *stride = 1* y *padding valid* (sin relleno), ¿Cual es el tamaño del mapa de salida
2. Calcula *solo* el valor de la esquina superior izquierda del mapa (la primera posicion del filtro). Muestra la suma de productos.
3. ¿Este kernel parece detectar bordes *verticales* u *horizontales*? Justifica mirando los signos.

**Resultados**

*Punto Numero 1*

Formula para calcular el tamaño de salida es:

Salida = ((N - F + 2P) / S) + 1

Donde:
- N = Tamaño de la imagen (5x5 = 5)
- F = Tamaño del kernel (3x3 = 3)
- P = No hay relleno (0)
- S = Desplazamiento del filtro (1)

Realizando las debidas sustituciones, resultaria:

Salida = ((5 - 3 + 2(0) / 1) + 1) = 3

Se obtiene un mapa de salida de 3x3, esto es debido a que el kernel puede colocarse en tres posiciones horizontales y tres verticales.

*Punto Numero 2*
- X1 = (0 * 1) + (0 * 0) + (1 * -1) + (0 * 1) + (1 * 0) + (2 * -1) + (1 * 1) + (2 * 0) + (3 * -1)
- X1 = 0 + 0 + -1 + 0 + 0 + -2 + 1 + 0 + -3
- X1 = -5

El valor de la esquina superior izquierda es **-5**

*Punto Numero 3*

Detecta principalmente bordes verticales. Porque el filtro compara los valores del lado izquierdo con los del lado derecho de una region de la imagen. Si existe un cambio importante de intensidad entre ambos lados, puede producir una respuesta de gran magnitud.

# Pregunta 2 - Contar pesos

## *Una imagen RGB de **28x28x3**. Compara dos modelos:*
- *Modelo A (MLP ingenuo):* Aplastas la imagen a un vector y conectas *todas* las entradas a una capa densa de *64 neuronas* (sin bias por ahora).
- *Modelo B (CNN):* Una `Conv2D` con *16 filtros* de *3x3*, `padding''same`=, sobre la misma imagen (con bias: un bias por filtro).

**Tareas**
1. ¿Cuántos pesos tiene la capa densa del Modelo A? (Fórumla y número).
2. ¿Cuántos parámetros tiene la Conv2D del Modelo B? (pesos de kernels + biases).
3. En **una frase*: ¿Por que la CNN suele generalizar mejor con el mismo número de imágenes de entrenamiento?

**Resultados**

*Punto Numero 1*

Aplanar la imagen para convertirla en un vector:
- 28 X 28 X 3 = 2352

Por tanto se tiene **2352** valores de entrada.

Cada una de las 64 neuronas se conectan a las 2352 entradas, por ello se multiplican.
- PESOS = ENTRADAS X NEURONAS
- PESOS = 2352 X 64
- PESOS = 150, 528

La capa densa tiene **150, 528 pesos** sin contar bias.

*Punto Numero 2*

Se tiene una capa **Conv2D** con 16 filtros de 3X3, aplicada a una imagen RGB de 3 canales y con un bias por filtro.

Cada filtro debe considerar los 3 canales de la imagen:
- 3 X 3 X 3 = 27

Cada filtro tiene 27 pesos.

Calcular los pesos en los 16 filtros:
- 27 X 16 = 432

Cada uno de los 16 filtros tiene un bias:
- 432 + 16 = 448

La capa convolucional tiene 448 parámetros en total, de los cuales 432 son pesos de los kernels y 16 son biases.

***El padding="same" permite conservar las dimensiones espaciales de la imagen de entrada cuando el stride es 1, pero no modifica el número de parámetros.***

*Punto Numero 3*

La CNN suele generalizar mejor porque utiliza filtros compartidos que necesitan muchos menos parametros y aprovechan la estructura espacial de la imagen, reduciendo el riesgo de sobreajuste con la misma cantidad de imagenes de entrenamiento.

# Pregunta 3 - ¿Qué cambia si meto más capas?

## Parte del notebook `CNNriesgo` (Simplificado):

**Entrada (21x28x3)**
- Conv2D(32, 3x3, same) + LeakyReLU
- MaxPool(2x2)
- Flatten -> Dense(32) -> Dense(nClasses, softmax)

## Quieres *apilar un segundo blque* convolucional *antes* del Flatten:
- ... -> Conv2D(32) -> Pool -> Con2D(64, 3x3, same) -> Pool -> Flatten -> ...

**Tareas**
1. Tras el *primer* MaxPool(2×2) con padding same sobre 21×28, ¿qué tamaño aproximado (alto×ancho) esperas? (puedes redondear / usar la regla “casi la mitad”)
2. ¿Qué *significan* ahora los 64 filtros de la segunda Conv2D: detectan bordes “crudos” o patrones *más compuestos*? Explica con la analogía de la lupa / capas abstractas.
3. Riesgo: si añades *muchas* capas Conv+Pool con pocas imágenes, ¿qué falla típico verías en las curvas train vs validation? ¿Qué harías primero para mitigarlo (Dropout, más datos, menos filtros…)? Elige *una* medida y justifica.

**Resultados**

*Punto Numero 1*

Se tiene una imagen de entrada de:
- 21 x 28 x 3

Primero pasa por una convolucion Conv2D(32, 3x3, same).

Como se utiliza padding=same, se conserva el alto y el ancho
- 21 x 28 x 32

Despues se aplica MaxPool(2x2). *MaxPooling reduce aproximadamente a la mitad las dimensiones espaciales:*
- Alto: 21 / 2 = 10.5, aproximadamente 11.
- Ancho: 28 / 2 = 14.

Por tanto:
- 11 x 14

Como se tiene 32 filtros, la salida completa seria:
- 11 x 14 x 32

Se espera un tamaño aproximado de 11×14 píxeles, conservando los 32 canales de características.

*Punto Numero 2*

Utilizando la analogía de la lupa, se puede imaginar que, cada bloque convolucional funciona como una lupa que analiza progresivamente mas detalles. Se podria ver del siguiente modo:
- En la primera capa, se observan detalles basicos, como lineas y bordes.
- En la segunda capa, combina esos detalles para identificar formas, texturas y patrones mas elaborados.
- Con capas posteriores, puede combinar esos patrones para reconocer partes de objetos o caracteristicas mas abstractas.

Por lo tanto los 64 filtros de la segunda Conv2D detectan patrones mas compuestos, porque trabajan con las caracteristicas extraidas por la primera convolución y no directamente con los pixeles originales.

*Punto Numero 3*

El principal riesgo es cuando se tiene pocas imagenes de entrenamiento es el sobreajuste **(Overfitting)**

*Esto ocurre cuando el modelo aprende demasiado bien las imagenes de entrenamiento, incluyendo detalles particulares que no necesariamente se repiten en imagenes nuevas*

***¿Como identificarlo?***
- *Entrenamiento:* La perdida continua disminuyendo y la precision aumenta.
- *Validacion:* La perdida comienza a aumentar y la precision deja de mejorar o disminuye.

***¿Como mitigarlo?***

Aumentar los datos de entrenamiento mediante **Data Augmentation**, ya que al generar variaciones de las imagenes originales como rotaciones pequeñas, desplazamientos, cambios moderados de brillo, etc, el modelo aprende a reconocer las caracteristicas importantes sin depender demasiado de detalles especificos de las imagenes originales.

# Pregunta 4 - Formas: de volumen a vector

## Supón que, justo antes del Flatten, el tensor tiene forma `(7, 7, 64)` (lote omitido: una sola imagen).

**Tareas**
1. ¿Cuantos numeros salen del Flatten? (un solo entero)
2. Si la siguiente Dense tiene *32 neuronas* (con bias), ¿Cuantos parametros tiene *esa* Dense?
3. Si en vez de Flatten usas *Global Average Pooling* (un promedio por canal), ¿Que forma tendrias a la salida y cuantos valores serian? ¿Ventaja frente a Flatten cuando la imagen de entrada es mas grande?

**Resultados**

*Punto Numero 1*

*Flatten* se encarga de convertir todas esas dimensiones en un unico valor. Por lo que se multiplican los valores:
- 7 x 7 x 64 = 3136

Se obtienen 3, 136.

*Punto Numero 2*
- Parametros = (entradas x neuronas) + bias

Se tiene:
- Entradas = 3136.
- Neuronas = 32.
- Biases = 32. **(Uno por neurona)**

Se sustituye:
- Parametros = (3136 x 32) + 32
- Parametros = 100384

La capa Densa tiene 100, 384 parametros.

*Punto Numero 3*

*GAP* o *Global Average Pooling* calcula el promedio de todos los valores espaciales de cada canal

Dado que se tiene un tensor de:
- (7, 7, 64)

Significa que existen 64 canales, cada uno con una matriz de 7x7

GAP calcula un promedio por canal.
- Promedio = suma de los 49 valores / 49

Por lo que:
- Canal 1 -> Promedio
- Canal 2 -> Promedio
- De esta manera hasta llegar al ultimo canal

Contendria unicamente 64 valores.

*Ventaja frente a Flatten*

Global Average Pooling reduce considerablemente la cantidad de valores que pasan a las capas densas. Esto es especialmente util cuando trabajamos con imagenes mas grandes, porque Flatten conserva todas las posiciones espaciales y genera vectores mucho más grandes, mientras que GAP mantiene un unico valor por canal. Como consecuencia, podemos reducir los parametros de las capas densas y disminuir el riesgo de sobreajuste.

# Pregunta 5 - Softmax y el error "casi seguro"

## Una CNN de 3 clases (inundacion, incendio, tornado) saca logits que, tras softmax, dan:
- P = [0.10, 0.05, 0.85]

**La etiqueta verdadera (one-hot) es `[0, 1, 0]` (incendio).**

**Tareas**
1. ¿Qué clase predice el modelo (`argmax')?
2. ¿Está “seguro” o “confundido”? Usa los números, no adjetivos vacíos.
3. Sin calcular la fórmula exacta: argumenta si la *categorical crossentropy* de este ejemplo será *alta* o *baja*, y por qué (pista: castiga cuando la probabilidad de la clase correcta es pequeña).

**Resultados**

*Punto Numero 1*

Teniendo las probabilidades y sus clases ordenadas:
- Inundacion = 0.10 (10%)
- Incendio = 0.05 (5%)
- Tornado = 0.85 (85%)

*argmax* selecciona la posicion que contiene el valor mas alto. Para el caso:
- argmax(P) = argmax(0.10, 0.05, 0.85) = 2

Por lo que, argmax predice la clase **Tornado**, con una probabilidad del 85%

*Punto Numeero 2*

Dado que el modelo asigna un 85% de probabilidad a Tornado, mientras que solamente asigna un 5% a Incendio, que es la clase verdadera. Esto significa que existe una diferencia de 80 puntos porcentuales entre la clase que predice y la clase correcta.

Por lo que el modelo esta bastante seguro de su prediccion, pero se equivoca, ya que asigna un 85% a Tornado y solamente un 5% a la clase correcta Incendio.

*Punto Numero 3*

*Categorical Crossentropy* mide qué tan diferentes son las probabilidades predichas por el modelo respecto a las etiquetas verdaderas.

En esta practica:
- Prediccion = [0.10, 0.05, 0.85]
- Etiqueta verdadera = [0, 1, 0]

Dado que la etiqueta verdadera indica que la segunda clase es la correcta y el modelo asigno solamente el 5% de probabilidad y, justamente esta funcion de perdida castiga precisamente el comportamiento de asignar una probabilidad muy pequeña a la clase correcta es que se puede definir que la **perdida sera alta**

# Pregunta 6 — Padding, stride y “se me achicó la imagen”

## Entrada *32×32*, kernel *5×5*, *un* filtro, *un* canal.

**Tareas**

*Completa la tabla (escribe el alto×ancho de salida):*

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   padding  stride  salida (alto×ancho) 
  ──────────────────────────────────────
   valid         1                      
   valid         2                      
   same          1                      
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Luego: si encadenas *tres* MaxPool(2×2) seguidos sobre una imagen 32×32 (sin cuidar bordes), ¿qué problema práctico aparece para clasificar objetos *pequeños* o detalles finos?

**Resultados**

*Punto Numero 1*

Se tienen los siguientes datos:
- Imagen de entrada: 32 x 32.
- Kernel: 5 x 5.
- Numero de filtros: 1.
- Canales: 1.

Para calcular las dimensiones de salida se utiliza:
- O = ((N - F + 2P) / S) + 1

Donde:
- N: Tamaño de entrada.
- F: Tamaño del kernel.
- P: Cantidad del padding.
- S: Stride.
- O: Tamaño de salida.

*Para el primer valor: valid y stride = 1*

**Con valid no se agrega relleno, por lo que P = 0**
- O = ((32 - 5 + 0) / 1 ) + 1
- O = 27 + 1 = 28

**Se obtiene una salida de 28 x 28**

*Para el segundo valor: valid y stride = 2*
- O = ((32 - 5) / 2) + 1
- O = 13.5 + 1.
- O = 14 **(Se redondea hacia abajo)**

**Se obtiene una salida de 14 x 14**

*Para el tercer valor: same y stride = 1*

**Con same se agrega relleno para conservar las dimensiones espaciales de la entrada cuando el stride es 1**

Por lo que:
- O = 32.

**Se obtiene una salida de 32 x 32**

***Tabla Final***

| Padding | Stride | Salida (altoxancho) |
|---------|--------|---------------------|
| valid | 1 | 28 x 28 |
| valid | 2 | 14 x 14 |
| same | 1 | 32 x 32 |

*Punto Numero 2*

**Cada *MaxPool(2x2)* reduce aproximadamente a la mitad el alto y el ancho.** Por lo que al tener una imagen de *32 x 32* esta iria cambiando del siguiente modo:
- Imagen original: 32 x 32.
- Primer MaxPool: 16 x 16.
- Segundo MaxPool: 8 x 8.
- Tercer y ultimo MaxPool: 4 x 4.

La imagen terminaria con dimensiones de *4 x 4*

*Por tanto al reducir demasiado las dimensiones espaciales, podemos perder informacion importante sobre los detalles pequeños de la imagen, esto dificultando su clasificacion.*

# Pregunta 7 — Dropout: ¿dónde y para qué?

## En `CNNriesgo' hay `Dropout(0.5)' después del pooling y otra vez antes de la salida.

**Tareas**
1. Durante *entrenamiento*, ¿qué hace Dropout(0.5) en una capa densa de 32 neuronas (en promedio cuántas “sobreviven” por paso)?
2. Durante *inferencia* (`predict'), ¿se apagan neuronas al azar? ¿Por qué sí o no?
3. Un compañero pone Dropout *solo* en la última época “para que no se sobreajuste al final”. ¿Tiene sentido? Critica la idea en 3–5 líneas.

**Resultados**

*Punto Numero 1*

**El valor 0.5** significa que existe una probabilidad del 50% de que cada neurona sea desactivada temporalmente durante cada paso de entrenamiento

Por lo que se tiene:
- Neuronas totales: 32.
- Porcentaje que se desactiva: 50%
- Porcentaje que permanece activo: 50%

Se realiza un pequeño calculo:
- 32 x 0.5 = 16

En promedio **sobreviven 16 neuronas** y **las otras 16 se desactivan** temporalmente durante cada paso de entrenamiento. *La seleccion de que neuronas se desactivan y activan, cambia aleatoriamente.*

*Punto Numero 2*

Cuando se utiliza un modelo para realizar predicciones como **predict()**, Dropout deja de desactivar enuronas de forma aleatoria.

Esto es debido a que, durante la inferencia se necesita que el modelo utilice todas las neuronas aprendidas para generar sus predicciones. Durante el entrenamiento, Dropout ayuda a evitar que el modelo dependa demasiado de ciertas neuronas, cosa diferente durante la inferencia que es donde se utiliza la red completa.

*Punto Numero 3*

Dado que el Dropout consiste en prevenir el sobreajuste durante todo el proceso de aprendizaje, no llega a tener mucho sentido aplicarlo unicamente en la ultima epoca. Si se llegase a aplicar este ajuste, el modelo se habra entrenado practicamente todo el tiempo sin la regularizacion, habria sido como si nunca se hubiera aplicado el Dropout y por lo tanto, no se habria aprovechado adecuadamente su beneficio.

# Pregunta 8 — Diseño: 5 clases de animales

## Debes adaptar `CNNriesgo' a: ranas, arañas, monos, ballenas, pájaros.

**Tareas**
1. ¿Cuántas neuronas debe tener la *última* Dense y qué activación? ¿Por qué?
2. Si todas las fotos entran a *224×224×3* pero el modelo tiene `input_shape=(21,28,3)', ¿qué *debe* pasar antes del `fit'? (una frase operativa)
3. Propón *una* mejora de arquitectura (segundo Conv, BatchNorm, data augmentation…)  y di *qué síntoma* en train/val te haría pensar que esa mejora era necesaria.

**Resultados**

*Punto Numero 1*

Dado que se tienen 5 clases:
- Ranas.
- Arañas.
- Monos.
- Ballenas.
- Pajaros.

Se podria definir para **la ultima capa Dense contener 5 neuronas, una por cada clase**, ademas de utilizar la activacion **softmax**

Esto porque *softmax* convierte los valores de salida del modelo en probabilidades que representan **que tan probable es que una imagen pertenece a cada clase.** En una prueba podriamos obtener diferentes probabilidades para cada clase, teniendo un resultado final de 1 o 100% y seleccionando a la clase con la probabilidad mas alta.

*Punto Numero 2*

Dado que se tiene una diferencia de dimensiones de entrada, se debe realizar un redimensionamiento para que todas las imagenes tengan las dimensiones esperadas por la CNN.

Para el caso, se puede utilizar en *TensorFlow/Keras*:

```python
tf.image.resixe(imagenes, (21, 28))
```

Asi las imagenes pasarian de **224 x 224 x 3** a **21 x 28 x 3**

*Punto Numero 3*

Se propondria agregar un **segundo bloque convolucional *Conv2D* antes de las capas densas**

Esto porque la primera capa convolucional puede aprender caracteristicas sencillas, como bordes y texturas, mientras que la segunda puede combinar esas caracteristicas para identificar patrones mas complejos, como formas y partes de los animales.

*¿Que sintoma justificaria este mejora?*

Si se llegase a observar que tanto la precision como la validacion del entrenamiento son bajas y las perdidas de emabas permanecen altas, podria existir subajuste. Esto indicaria que el modelo posiblemente no tiene suficiente capacidad para aprender las caracteristicas necesarias de las cinco clases.

Agregar otro bloque convolucional podria ayudar a aprender caracteristicas mas complejas.

# Pregunta 9 — CNN vs MLP vs RNN (mismo problema, mala herramienta)

## Tres escenarios. Elige *CNN*, *MLP* o *RNN/Transformer* y justifica en *una* frase cada uno:

**Tareas**
1. Predecir si un alumno aprueba con promedio, faltas y horas de estudio (tabla).
2. Clasificar fotos de semáforo (rojo / amarillo / verde).
3. Autocompletar la siguiente línea de código dado el prefijo escrito.

Si aplastas la foto del semáforo y usas un MLP “grande”, ¿puede *aprender*? ¿Qué sacrificas respecto a una CNN? (parámetros, datos, invariancia…)

**Resultados**

*Punto Numero 1*

Se cuenta con informacion organizada en una tabla, tal como:
- Promedio.
- Numero de faltas.
- Horas de estudio.

Dado que sus datos son tabulares se puede aprovechar mejor un **MLP**, ya que la red puede aprender relaciones entre las diferentes variables para determinar si un alumno aprueba o reprueba.

*Punto Numero 2*

Considerando que un semaforo cuenta con tres estados, se puede clasificar sus imagenes en tres categorias:
- Rojo.
- Amarillo.
- Verde

Dado que su representacion es totalmente visual y diferenciada por colores, se utilizaria **CNN** porque esta diseñada para procesar imagenes y reconocer caracteristicas visuales como colores, formas y patrones espaciales.

*Punto Numero 3*

Teniendo un fragmento de codigo y se quiere predecir que linea podria continuar, convendria mas utilizar **RNN o un Transformer**, esto debido a que, pueden procesar secuencias de texto y aprender relaciones entre palabras, instrucciones y fragmentos de codigo anteriores para predecir lo siguiente.

*Punto Numero 4*

Si, un **MLP grande** puede aprender a clasificar imagenes de semaforos, incluso si primero convertimos cada fotografia en un vector mediante **Flatten**

Por desgracia, existe una desventaja. **Al aplanar la imagen**, perdemos la estructura espacial que permite identificar facilmente las relaciones entre los pixeles vecinos.

*¿Que se estaria sacrificando con respecto a un CNN?*
- **Mayor cantidad de parametros**. El **MLP** necesita conectar las entradas con sus neuronas, lo que puede generar una cantidad considerable de pesos.
- **Necesidad de mas datos**. Al tener mas parametros y no aprovechar directamente la estructura espacial, puede llegar a necesitar de mas imagenes para aprender correctamente.
- **Menor invariacia espacial**. Un **CNN** llega a utilizar filtros compartidos que pueden rconocer caracteristicas similares en distintas posiciones de una imagen, mientras que un **MLP** no aprocecha naturalmente esta propiedad.

# Pregunta 10 — Experimento mental: mover un gato

## Entrenaste una CNN que detecta “hay un gato” en fotos 64×64. En el test, el mismo gato aparece *corrido 10 píxeles a la derecha*, mismo fondo, misma escala.

**Tareas**
1. ¿Por qué una CNN tiene *más chance* de seguir acertando que un MLP que ve el vector aplastado? (pesos compartidos / detección local)
2. Si en vez de correrlo lo *giraras 90°* y nunca viste gatos de lado en el train, ¿la CNN “mágica” garantiza acierto? ¿Qué haría falta (augmentation, más datos…)?
3. Escribe *una* pregunta que tú le harías a un compañero para comprobar si entendió qué son los *pesos del kernel* (no copies las de arriba).

**Resultados**

*Punto Numero 1*

La **CNN** tiene mas probabilidades de reconocerlo debido a dos caracteristicas importantes:
- **Pesos compartidos**: Los filtros convolucionales utilizan los mismos pesos mientras recorren diferentes regiones de la imagen.
- **Deteccion local**: Los filtros pueden identificar caracteristicas como bordes, orejas, ojos y texturas, independientemente de que aparezcan en diferentes posiciones.

Si por ejemplo, durante el entrenamiento la **CNN** aprendio a reconocer las orejas de un gato, puede detectar caracteristicas similares aunque estas se encuentren desplazadas alunos pixeles de su posicion original. En cambio un **MLP** trabaja con un vector aplanado y no puede aprovechar directamente la estructura espacial de la imagen.

*Punto Numero 2*

Si nunca observo gatos girados durante el entrenamiento, podria tener dificultades para reconocerlos cuando aparezcan en una orientacion diferente.

Esto se debe porque, aunque las **CNN** puede reconocer caracteristicas en diferentes posiciones, eso no significa que sean automaticamente invariantes ante rotaciones.

*¿Que se necesita para mejorar el reconocimiento?*

Una posible solucion seria utilizar **Data Augmentation**, generando variaciones de las imagenes originales mediante:
- Rotaciones.
- Desplazamientos.
- Cambios moderados de escala.
- Variaciones de iluminacion.

De esta manera, durante el entrenamiento la **CNN** tendria la oportunidad de aprender que un gato sigue siendo un gato aunque cambie su orientacion o posicion.

*Punto Numero 3*

Una posible pregunta seria:
- *Si modificamos loa valores de los pesos de un kernel convolucional durante el entrenamiento, ¿Como podria cambiar la caracteristica que detecta ese filtro en una imagen? Explica con un ejemplo*