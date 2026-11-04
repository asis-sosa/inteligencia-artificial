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

  └────