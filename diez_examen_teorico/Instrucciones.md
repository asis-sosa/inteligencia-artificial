# EXAMEN TEÓRICO — PERCEPTRÓN, MLP Y CNN (GRUPO B)

### 1 Datos del alumno
══════════════════

  ━━━━━━━━━━━

   Nombre  Sebastian Asis Sosa Santiago
   Grupo   B 
   Fecha   XX / XX / 2026

  ━━━━━━━━━━━


### 2 Pregunta 1 — Por qué no basta “una sola neurona”
══════════════════════════════════════════════════

  1. Resume el funcionamiento de un perceptrón como “regla de decisión”.
  2. Explica la noción de *frontera lineal* sin escribir fórmulas.
  3. Da un ejemplo (aunque sea inventado) donde esa frontera *no*
     alcanza.


2.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Punto Numero Uno:
    El funcionamiento de un perceptron como "Regla de Decisión" se debe a su estructura y en como esta construido, debido al consumo de informacion relevante, la manera en como la utiliza para clasificarla y finalmente con el resultado tomar una eleccion. El perceptron no trabaja de forma alazar, sino que con las formulas que utiliza, encuentra una respuesta numerica que decide.
    - Punto Numero Dos:
    La nocion de "Frontera Lineal" radica en un lineamiento que separa las categorias o grupos de datos que cuentan con informacion similar entre si formando una separacion clara entre ambos grupos. Esta linea fronteriza, terminaria por representar un punto final para ambos grupos.
    - Punto Numero Tres:
    Un ejemplo seria donde se intentaria clasificar altura y peso, y se tuviera casos donde hubiera datos en donde hay hombres o mujeres alto y gordos, pequeños y gordos, altos y delgados, pequeños y delgados y, no se tuviera una clasificacion adecuada de los involucrados.

  └────


### 3 Pregunta 2 — CNN: de píxeles a mapas
══════════════════════════════════════

  1. ¿Qué problema de *estructura espacial* ignora un MLP si aplana la
     foto?
  2. ¿Qué significa que un mismo filtro se aplique en toda la imagen?
  3. Además de clasificación de objetos, cita *dos* usos donde la CNN
     encaja bien.


3.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Punto Numero Uno:
    El problema que se encuentra es el hecho de que el MLP, al aplanar la imagen, considera los valores simultaneos, dejando de lado contextualizaciones que puede tener la imagen por su orden en dos dimensiones, de forma natural, el MLP podria ignorar, bordes, formas y figuras de la imagen, por no considerarlos en su forma de trabajar.
    - Punto Numero Dos:
    Significa que el mismo filtro o kernel es reutilizado en toda la imagen, sin alterar sus valores, para identificar ciertas caracteristicas.
    - Punto Numero Tres:
    Para la clasificacion de indentificacion de rostros y Segmentacion de regiones en una imagen, identificar hasta donde llegan un edificio, una carretera o cualquier otra region de un lugar.

  └────


### 4 Pregunta 3 — Softmax, clases y decisiones
═══════════════════════════════════════════

  1. Diferencia un problema *binario* de uno *multiclase* en términos de
     salida de la red.
  2. ¿Qué lectura le das a las probabilidades que produce un softmax?
  3. Imagina tres carpetas de imágenes (tres riesgos o tres animales):
     ¿qué arquitectura de *salida* usarías y por qué?


4.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Numero Uno:
    Utilizando el peso para ambos casos, en el "binario" seria para definir delgado o gordo, solo de forma superficial, si se quisiera con mas detalles el analisis, para "multiclase" seria definir sobrepeso, peso ideal / normal, bajo de peso, aqui se tendria que aprovechar de los valores para definir exactamente donde entraria.
    - Nunero Dos:
    Un valor porcentual que define que tan probable es que el objeto que se este definiendo pertenezca a cierta categoria, dependiendo de la confiabilidad del dataset que permita identificar al objeto.
    - Numero Tres:
    Utilizaria una arquitectura multiclase, ya que al ser tres carpetas, cada una con su respectivo dataset, se neceita mas de una neurona para definir si una imagen con algun desastre pertenece a alguno de los tres dataset que ya se cuenta y definir que tanto porciento de similitud tienen entre si.

  └────


### 5 Pregunta 4 — MLP: profundidad con sentido
═══════════════════════════════════════════

  1. ¿Qué ganas al apilar capas densas con activaciones no lineales?
  2. ¿Qué riesgo aparece si la red es *demasiado* grande para tus datos?
  3. Relaciona “capa oculta” con la idea de aprender representaciones
     intermedias (en palabras simples).


5.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Numero Uno:
    Lo que se obtiene es una mayor confiabilidad en el aprendizaje del modelo al contemplar mas oportunidad de que aprenda caracteristicas mas complejas que con una visulizacion lineal no podria comprender del todo
    - Numero Dos:
    El mator riesgo al tener una red demasiado grande es que el mismo modelo, llegue a aprender caracteristicas que para el procesamiento final, podrian no ser totalmente utiles para la finalidad, consideraria elementos especificos de los datos de entrenamiento que para las pruebas podria fallar por no contar con esas similitudes.
    - Numero Tres:
    Las "capas ocultas" son las que trabajar progresivamente los datos para transformarlos a informacion util para el objetivo y es justo donde entra la "representacion intermedia" entra, ya que es esta la permite identificar lo que realmente es relevante para las trasnformaciones. Ambos funcionan para tener los datos, transformarlos progresivamente y obtener patrones importantes.
    
  └────


### 6 Pregunta 5 — Entrenamiento sin magia
══════════════════════════════════════

  1. Explica qué es una *época* a nivel intuitivo.
  2. ¿Hacia qué “objetivo” se mueven los pesos cuando hablamos de
     minimizar el error?
  3. Si el learning rate es absurdo (muy grande o muy chico), ¿qué
     síntomas conceptuales esperarías?


6.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Punto Numero Uno:
    Las epocas son como vueltas que da el modelo para aprender sobre los datos, cometer errores, aprender de esos errores y seguir aprendiendo sobre los datos para concluir con la informacion mas viable.
    - Punto Numero Dos:
    Va hacia el objetivo de obtener un valor cercano hacia rel resultado esperado, mediante el "loss function" se va determinando que tan separado nos encontramos de lo que se espera, basado en el y en diferente aspectos se alteran los pesos para modificar el valor resultante y acercanos al resultado que se espera.
    - Punto Numero Tres:
    Puede llegar ser poco util la funcion de perdida, provocando que el error oscile o inclusive llegue a aumentar, podria el entrenamiento volverse inestable, eso del lado de lo absurdo muy grande, al contrario, el entrenamiento puede llegar a ser muy lento, se necesitarian muchas iteraciones para intentar reducir el error, puede llegar a provocar que el modelo no este aprendiendo de la forma correcta.

  └────


### 7 Pregunta 6 — Bloques de una CNN
═════════════════════════════════

  Sin matemáticas, di el papel de cada pieza:
  1. Kernel / filtro convolucional
  2. Función de activación después de conv
  3. Max pooling
  4. Capa densa + softmax al final de un clasificador


7.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Punto Numero Uno:
    Funciona para verificar region por region de una imagen para identificar caracteristicas clave en ella.
    - Punto Numero Dos:
    Determinar no linealidad despues de la convolucion para relacionar caracteristicas mas complejas.
    - Punto Numero Tres:
    Reducir las dimensiones espaciales conservando la caracteristica con valor mas alto, para de este modo reducir la informacion de analisis.
    - Punto Numero Cuatro:
    La capa densa toma la informacion de los procesos anteriores para combinarlas y determinar una puntuacion, puntuacion que, softmax aprovecha para convertir en probabilidades, las cuales determinan un categoria, concluyendo en dos situaciones, una suma total de probabilidades de 1 y teniendo una categoria ganadora con la mayor probabilidad adquirida.
  └────


### 8 Pregunta 7 — XOR y la historia del aprendizaje
════════════════════════════════════════════════

  1. ¿Por qué XOR se volvió un “contraejemplo” famoso?
  2. ¿Qué elemento de un MLP permite patrones que no son una sola línea?
  3. ¿En qué tipo de tabla/problema del mundo real seguirías usando algo
     tan simple como un perceptrón o un modelo lineal?


8.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Punto Numero Uno:
    Debido a su estructura, XOR demuestra puntos en los que, si se considera mediante redes neuronales, se encuentran en polos opuestos, lugares donde la frontera lineal no es suficiente para separar ambas categorias, esto demostrando una importante limitaciones de los perceptrones.
    - Punto Numero Dos:
    La implementaciones de las capas ocultas y las activaciones no lineales, permite al MLP aprender patrones mas complejos.
    - Punto Numero Tres:
    Una situacion financiera sencilla, donde se estaria analizando ingresos y egresos, para definir que tan bien se esta administrando las finanzas presentes.

  └────


### 9 Pregunta 8 — De lo simple a lo abstracto en visión
════════════════════════════════════════════════════

  1. Contrasta lo que buscan capas tempranas vs capas profundas en una
     CNN.
  2. ¿Qué intuición da eso para *transfer learning* (aunque no lo hayas
     programado)?
  3. ¿Cuándo sospecharías que tu CNN es “profunda de más” para el
     dataset del curso?


9.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Punto Numero Uno:
    Las primeras capas lo que buscan son simples patrones en las imagenes, como figuras, algunas texturas o distincion de colores, conforme se va avanzando entre las capas, llegando a las ultimas capas o las profundas se combinan las caracteristicas vistas en las primeras capas para formar figuras mas complejas e identificar lo que contiene la imagen.
    - Punto Numero Dos:
    Que, basicamente aprovecha cierta informacion aprendida de otros entrenamientos, para posteriormente integrar nuevas adaptaciones y pueda lograr otras tareas que en los entrenamientos anteriores no lo haria. Seria como reautilizar un formato de alguna actividad en otra, para no tener que hacerlo desde cero.
    - Punto Numero Tres:
    Cuando al estar analizando el rendimiento del modelo, se puede identificar ciertas aspectos que no coinciden del todo con lo optimo, como identificar un desajuste entre la precision del entrenamiento y la validacion, contar con pocos datos de entrenamiento o inclusive tomar la desicion de ir directamente a una red profunda, sabiendo requiere de demasiada memoria, procesamiento y tiempo.

  └────


### 10 Pregunta 9 — Análisis: matching problema → modelo
════════════════════════════════════════════════════

  Elige *Perceptrón/lineal* / *MLP* / *CNN* (una opción) y justifica en
  una frase:

  1. Predecir “compra / no compra” con edad, ingreso y visitas a la web
     (columnas numéricas).
  2. Detectar si hay un gato en una foto.
  3. Aproximar una frontera “curva” o a trozos en datos 2D tabulares.
  4. ¿CNN es la herramienta natural para predecir la siguiente palabra
     de un párrafo? Justifica y nombra una familia del curso más
     adecuada (RNN/Transformer a nivel nombre).


10.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Punto Numero Uno:
    "Perceptron/lineal", dado que el analisis es simple y solo se define entre si compra o no compra ("1" o "0"), el resultado final podria dividirse en una frontera lineal.
    - Punto Numero Dos:
    "CNN", dado que es la mejor herramienta para analizar imagenes con su estructura, utilizacion del kernel, convoluciones y capas que utilizan para definir que hay en cada region de pixeles.
    - Punto Numero Tres:
    "MLP", dado que lo que se quiere analizar es una curva en una tabla, un perceptron lineal no sera suficiente y como son datos tabulares, un analisis con CNN no sera necesario, la opcion de multiples perceptrones para analizar los datos que formarian una curva es la opcion mas razonable.
    - Punto Numero Cuatro:
    No, la mejor familia para lograr una prediccion de palabra en una secuencia de texto es la combinacion entre los RNN y Transformer, ya que ambos estan construidos para analizar texto, recodar contextos y poder predecir hacia donde se dirige el tema que se esta analizando.

  └────


### 11 Pregunta 10 — Análisis: auditoría de un equipo
═════════════════════════════════════════════════

  Un equipo entrega un modelo “muy preciso” en su laptop y falla con
  datos nuevos.

  1. ¿Qué diagnósticos conceptuales harías *antes* de tocar
     hiperparámetros al azar?
  2. Pide *dos* evidencias que deberían mostrar en la defensa (curvas,
     separación train/val, ejemplos de error, etc.).
  3. Redacta *tres* preguntas tuyas para comprobar si saben cuándo usar
     perceptrón, MLP o CNN (distintas a las del Grupo A si las conoces).


11.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────

    - Punto Numero Uno:
    Una de las primeras que se tendria que analizar seria el sobreajuste, verificar que el modelo este aprendiendo patrones de los datos y no memorizando exactamente los datos utilizados en el entrenamiento, igualmente verificar los datos de entrenamiento, se es necesario verificar que los datos utilizados contengan suficientes ejemplos diferentes o tambien que esten bien etiquetados, inclusive tambien no duplicar la informacion, verificar que los datos que se estan utilizando en el entrenamiento no sea exactamente los que se estan utilizando en las pruebas, esto podria influir de manera erronea en los errores del modelo.
    - Punto Numero Dos:
    Pediria como evidencia "Curvas de entrenamiento y validacion" y "Ejemplos de predicciones incorrectas", con ambas se podria analizar como se comportan las perdidas y precision durante las epocas y que situaciones provocan los errores.
    - Punto Numero Tres:
    1.- ¿Por que para el analisis de imagenes es mejor utilizar CNN que MLP o Perceptron/Lineal, que lo diferencia de ambos?
    2.- ¿Como puedes estar seguro que un Perceptron es mas que suficiente para el analisis de datos tabulares con algunas columnas? Detalla el funcionamiento del Perceptron.
    3.- ¿Indicame un ejemplo, de tu dia a dia, donde podrias aprovechar un MLP? Justifica tu respuesta.

  └────