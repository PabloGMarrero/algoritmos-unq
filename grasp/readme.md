# Metaheurística GRASP 

## Pre-requisitos
- Python 3.80
- numpy 
- mathplotlib.

Se deja un archivo requeriments.txt para ser ejecutado con el manejador de dependencias pip

## Como funciona?

### Entrada automática
Si no posee un grafo en particular puede utilizar los generados por el mismo programa. Para ello se deberá parar en la raiz del proyecto y ejecutar el comando
```python main.py {CANT_NODES} {LIMIT_BL} {MAX_ITERATIONS}```

donde 
- ```{CANT_NODES}``` corersponde a la cantidad de nodos para probar la instancia
- ```{LIMIT_BL}``` es el porcentaje de mejora para elegir el corte por busqueda local
- ```{MAX_ITERATIONS}``` la cantidad máxima de iteraciones para GRASP

Por ejemplo, si desea un grasp para 155 nodos, 1.2 porcentaje mejora y 500 iteraciones debe correr el comando
```python main.py 155 1.2 500```

### Entrada manual
En caso de tener una instancia y querer probarla lo que se debe hacer es dirigirse a la carpeta
```resources/``` y dejar un archivo .txt con el formato de nombre ```tex_graph_{CANT_NODES}.txt``` donde CANT_NODES es la cantidad de nodos de dicho grafo.
Debe respetar la siguiente estructura, ejemplo para un grafo de 16 nodos

```
16
0 127 465 441 384 269 457 179 533 556 291 724 928 148 580 71
127 0 373 903 81 792 357 261 852 10 588 891 311 947 942 45
465 373 0 972 13 556 746 444 556 952 762 13 583 163 674 316
441 903 972 0 437 687 421 897 366 625 68 525 830 75 315 721
384 81 13 437 0 549 278 313 831 59 822 93 432 119 346 599
269 792 556 687 549 0 693 488 206 112 207 238 986 57 954 321
457 357 746 421 278 693 0 421 237 350 129 600 769 501 529 103
179 261 444 897 313 488 421 0 807 476 443 416 243 785 780 117
533 852 556 366 831 206 237 807 0 78 357 659 875 495 484 931
556 10 952 625 59 112 350 476 78 0 186 444 491 538 874 229
291 588 762 68 822 207 129 443 357 186 0 818 254 165 951 540
724 891 13 525 93 238 600 416 659 444 818 0 208 337 147 362
928 311 583 830 432 986 769 243 875 491 254 208 0 382 140 253
148 947 163 75 119 57 501 785 495 538 165 337 382 0 674 203
580 942 674 315 346 954 529 780 484 874 951 147 140 674 0 472
71 45 316 721 599 321 103 117 931 229 540 362 253 203 472 0
68 97 11 6 2 39 90 22 95 36 29 72 89 92 57 78
```
Donde:
- La primera linea repesenta la cantidad de nodos
- De la segunda linea hasta la anteultima, la matriz de adyacencia 
- La ultima linea, un array con el costo de la tarea por cada nodo.

### Salida

Los distintos gráficos seran guardados en el directorio ```output/graphics/``` y ser irá creando un archivo para demostrar GRASP y otro archivo de BL con el siguiente nombre

- GRASP: ```grasp_start_{START_VERTEX}_rows_{CANT_NODES}_as_{LIMIT_BL}_max-iterations_{MAX_ITERATIONS}-{DATETIME}```
- BL: ```bl_{CANT_NODES}_as_{LIMIT_BL}_max-iterations_{MAX_ITERATIONS}-06-07-2023_10-32-38```

Donde
```{DATETIME}``` tiene formato ```dd-MM-yyyy_HH-MM-SS```
```{START_VERTEX}``` es el vertice por donde comenzó el greedy random