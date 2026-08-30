# Programas de Juguete (Canibales y Monjes, Laberinto y Conteo de Islas) **Resultados**

## Ejercicio Canibales y Monjes:

- 3C, 3S -- 0 -- 0,0
- 2C, 2S -> 1C, 1S -> 0, 0
- 2C, 2S -> 0,0 -> 1C, 1S
- 2C, 2S <- 1S <- 1C
- 2C, 3S <- 0 <- 1C
- 0C, 3S -> 2C -> 1C
- 0C, 3S -> 0 -> 3C
- 0C, 3S <- 1C <- 2C
- 1C, 3S <- 0 <- 2C
- 1C, 1S -> 2S -> 2C
- 1C, 1S -> 0 -> 2C, 2S
- 1C, 1S <- 1C, 1S <- 1C, 1S
- 2C, 2S <- 0 <- 1C, 1S
- 2C, 0S -> 2S -> 1C, 1S
- 2C, 0S -> 0 -> 1C, 3S
- 2C, 0S <- 1C <- 3S
- 3C, 0S <- 0 <- 3S
- 1C, 0S -> 2C -> 3S
- 1C, 0S -> 0 -> 2C, 3S
- 1C, 0S <- 1C <- 1C, 3S
- 2C, 0S <- 0 <- 1C, 3S
- 0C, 0S -> 2C -> 1C, 3S
- 0C, 0S -> 0 -> 3C, 3S

## Laberinto

Si existe la presencia de un objetivo final notificado, se puede utilizar la técnica de definir una trayectoria recta hacia la meta, ubicando el objeto movible hacia esa trayectoria, cambiando únicamente de la misma en el momento en que encuentre un bloqueo.
Si no existe la presencia de un objetivo final notificado, será definir el objeto movible que pase por todo el recorrido, recreando un mapa propio, donde defina por que zonas se puede acceder, donde están los bloques y demás objeto que impidan la trayectoria hasta el final.

## Conteo de Islas

```java
for(int i=0; i<n; i++){
	for(int j=0; j<n; j++){
		variable = matriz[i][j];
		if(variable == 1){
			if(matriz[i][j-1] == 2 || matriz[i-1][j] == 2 || matriz[i][j+1] == 2 || matriz[i+1][j] == 2){
				matriz[i][j] = 2; }
			else{
					matriz[i][j] = 2;
					islas++; }
		}else{}
    }
}
```