# Juego PyGame

### Indicaciones - Fase 1.

Basado en el codigo **"juego_pygame_mlp1.py"** analizar con diferentes neuronas los dataset recopilados

**Propuesta:** Se utilizara un total de 10 saltos en cada prueba, pero con diferentes resultados:
1. Un dataset con 10 saltos correctos.
2. Un segundo con 7 saltos correctos y 3 fallos.

Esto para apreciar el dataset con diferentes datos proporcionados y verificar los cambios entre pruebas y neuronas

**Propuesta:** Del mismo modo se utilizara diferente cantidad de neuronas para comparar los datos entre ellas:
1. Primera prueba con 2 capas, cada una con 3 neuronas y 300,000 iteraciones.
2. Segunda prueba con 1 capa, con 3 neuronas y 300,000 iteraciones.
3. Tercera prueba con 3 capas, con 3 neuronas cada una y 300,000 iteraciones.
4. Cuarta prueba con 2 capas, con 2 neuronas cada una y 300,000 iteraciones.
5. Quinta prueba con 2 capas, con 5 neuronas cada una y 300,000 iteraciones.
6. Sexta prueba con 2 capas, con 10 neuronas cada una y 300,000 iteraciones.

### Indicaciones Fase 2.

Basado en el mismo codigo **"juego_pygame_mlp1.py"** cambiar la estructura de redes neuronales **"MLP"** por **Arboles de decisión** y observar que tanto cambio se encuentran entre ambas tecnicas.

Se **Reutilizara** las mismas pruebas en relaciona saltos que en las pruebas anteriores, pero ahora solo se utilizara hasta 4 niveles de profundidad, los **Nombres para los datasets seguiran la misma estructura que el anterior**.

**Propuesta** Niveles de profundidad para las pruebas con arboles de decisión.
1. 3 Niveles de Profundidad
2. 1 Niveles de Profundidad
3. 2 Niveles de Profundidad
4. 4 Niveles de Profundidad

### Archivo DATASET

Aqui se mantiene todos los dataset recopilados, **utiliza la estructura "_X_Y" para indicar la prueba realizada, siendo Y la prueba en relacion a los saltos y X como la prueba en relacion a la cantidad de neuronas**