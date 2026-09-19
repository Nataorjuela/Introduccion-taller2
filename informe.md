# Informe del Taller 2

## Punto 1. Formulacion del problema

Para buscar una conexion entre Ana y Karen:

| Componente | Representacion en la red social |
|---|---|
| Estado inicial | Usuario `Ana` |
| Estado objetivo | Usuario `Karen` |
| Estados | Todos los usuarios del grafo |
| Acciones | Pasar de un usuario a uno de sus vecinos |
| Modelo de transicion | Si existe amistad `A-B`, desde `A` se puede ir a `B` |
| Prueba de objetivo | El usuario actual es `Karen` |
| Costo del camino | Una unidad por conexion recorrida |
| Solucion | Una ruta de usuarios desde `Ana` hasta `Karen` |

Respuestas:

1. Un nodo representa un usuario.
2. Una arista representa una relacion de amistad.
3. Expandir un usuario significa revisar sus vecinos y generar posibles siguientes estados.
4. Un nodo de busqueda debe contener usuario actual, padre, profundidad o costo y estado de visitado.
5. Se alcanza el objetivo cuando el usuario extraido de la frontera coincide con el destino.
6. Los grados de separacion son la cantidad de conexiones entre origen y destino.

## Punto 2. Construccion y analisis del grafo

| Usuario | Vecinos | Grado |
|---|---|---:|
| Ana | Bruno, Carla, Elena | 3 |
| Bruno | Ana, Diana, Felipe | 3 |
| Carla | Ana, Felipe, Gabriel | 3 |
| Diana | Bruno, Helena | 2 |
| Elena | Ana, Isabel | 2 |
| Felipe | Bruno, Carla, Helena | 3 |
| Gabriel | Carla, Jorge | 2 |
| Helena | Diana, Felipe, Karen | 3 |
| Isabel | Elena, Karen | 2 |
| Jorge | Gabriel, Karen | 2 |
| Karen | Helena, Isabel, Jorge | 3 |

Usuarios con mayor cantidad de conexiones: Ana, Bruno, Carla, Felipe, Helena y Karen, todos con grado 3.

No existen usuarios aislados en la red base. Todas las conexiones son bidireccionales.

Un usuario con muchas conexiones no garantiza que todas las rutas que pasan por el sean las mas cortas. La longitud depende de la posicion del usuario dentro del grafo y del destino buscado.

## Punto 3. Ejecucion manual de BFS

BFS usa cola FIFO y respeta el orden de vecinos del diccionario.

| N. | Extraido | Agregados | Cola despues de expandir | Visitados |
|---:|---|---|---|---|
| 1 | Ana | Bruno, Carla, Elena | Bruno, Carla, Elena | Ana, Bruno, Carla, Elena |
| 2 | Bruno | Diana, Felipe | Carla, Elena, Diana, Felipe | Ana, Bruno, Carla, Elena, Diana, Felipe |
| 3 | Carla | Gabriel | Elena, Diana, Felipe, Gabriel | Ana, Bruno, Carla, Elena, Diana, Felipe, Gabriel |
| 4 | Elena | Isabel | Diana, Felipe, Gabriel, Isabel | Ana, Bruno, Carla, Elena, Diana, Felipe, Gabriel, Isabel |
| 5 | Diana | Helena | Felipe, Gabriel, Isabel, Helena | Ana, Bruno, Carla, Elena, Diana, Felipe, Gabriel, Isabel, Helena |
| 6 | Felipe | - | Gabriel, Isabel, Helena | Ana, Bruno, Carla, Elena, Diana, Felipe, Gabriel, Isabel, Helena |
| 7 | Gabriel | Jorge | Isabel, Helena, Jorge | Ana, Bruno, Carla, Elena, Diana, Felipe, Gabriel, Isabel, Helena, Jorge |
| 8 | Isabel | Karen | Helena, Jorge, Karen | Ana, Bruno, Carla, Elena, Diana, Felipe, Gabriel, Isabel, Helena, Jorge, Karen |
| 9 | Helena | - | Jorge, Karen | Ana, Bruno, Carla, Elena, Diana, Felipe, Gabriel, Isabel, Helena, Jorge, Karen |
| 10 | Jorge | - | Karen | Ana, Bruno, Carla, Elena, Diana, Felipe, Gabriel, Isabel, Helena, Jorge, Karen |
| 11 | Karen | objetivo | - | Ana, Bruno, Carla, Elena, Diana, Felipe, Gabriel, Isabel, Helena, Jorge, Karen |

Ruta encontrada: Ana -> Elena -> Isabel -> Karen. Grados de separacion: 3. Nodos expandidos: 11. Frontera maxima: 4.

## Punto 4. Ejecucion manual de DFS

DFS usa pila LIFO. Como los vecinos se insertan en el orden del diccionario, el ultimo vecino agregado se explora primero.

| N. | Extraido | Agregados | Pila despues de expandir | Visitados |
|---:|---|---|---|---|
| 1 | Ana | Bruno, Carla, Elena | Bruno, Carla, Elena | Ana |
| 2 | Elena | Isabel | Bruno, Carla, Isabel | Ana, Elena |
| 3 | Isabel | Karen | Bruno, Carla, Karen | Ana, Elena, Isabel |
| 4 | Karen | objetivo | Bruno, Carla | Ana, Elena, Isabel, Karen |

Ruta encontrada: Ana -> Elena -> Isabel -> Karen. En este caso coincide con BFS, pero DFS no lo garantiza siempre.

## Punto 5. Implementacion de BFS

La funcion `buscar_conexion_bfs` esta en `busquedas.py`.

Puntos clave:

- usa `deque` como cola FIFO;
- marca visitados al generar vecinos para evitar duplicados;
- guarda `padres[vecino] = actual` para reconstruir la ruta;
- calcula grados como `len(ruta) - 1`;
- mide orden de expansion, nodos generados y frontera maxima.

## Punto 6. Implementacion de DFS

La funcion `buscar_conexion_dfs` esta en `busquedas.py`.

Puntos clave:

- usa una lista como pila LIFO;
- cada elemento guarda `(usuario, profundidad)`;
- respeta `limite_profundidad`;
- registra padres solo la primera vez que se genera un usuario;
- no garantiza ruta minima porque profundiza antes de probar todos los nodos del nivel actual.

## Punto 7. Pruebas de funcionamiento

Ejecute `python main.py` para generar los resultados de las seis consultas:

| Prueba | Origen | Destino |
|---:|---|---|
| 1 | Ana | Karen |
| 2 | Bruno | Jorge |
| 3 | Diana | Isabel |
| 4 | Gabriel | Elena |
| 5 | Felipe | Karen |
| 6 | Helena | Ana |

## Punto 8. Comparacion BFS y DFS

1. No siempre encuentran la misma ruta; depende del orden de vecinos.
2. BFS encuentra menos grados de separacion porque explora por niveles.
3. DFS puede expandir menos usuarios si el destino aparece temprano en su rama, pero tambien puede expandir mas.
4. BFS suele presentar frontera mas grande porque conserva todos los nodos del siguiente nivel.
5. El orden de vecinos afecta la primera ruta encontrada, especialmente en DFS.
6. Sin visitados, el algoritmo puede entrar en ciclos, por ejemplo Ana -> Bruno -> Ana.
7. BFS garantiza menos conexiones porque revisa primero todas las rutas de longitud 0, luego 1, luego 2, etc.
8. Si, DFS puede encontrar primero una ruta mas larga.
9. El limite de profundidad evita busquedas demasiado profundas, pero puede impedir hallar una solucion existente.
10. Para calcular grados de separacion conviene BFS.

## Punto 9. Usuarios sin conexion

Se agrega un componente separado:

```python
red_social["Laura"] = ["Mateo"]
red_social["Mateo"] = ["Laura"]
```

Al buscar Ana -> Laura, BFS y DFS vacian la frontera tras visitar el componente de Ana. Como Laura pertenece a otro componente, nunca se genera. El programa retorna `encontrado = False` y el mensaje `No existe conexion entre los usuarios`.

## Punto 10. Modificacion de la red

Se agregaron usuarios ficticios: Laura, Mateo, Nora, Oscar, Paula, Juan y Rosa.

Conexiones agregadas:

- Laura - Mateo
- Mateo - Nora
- Nora - Oscar
- Oscar - Paula
- Paula - Juan
- Juan - Laura
- Nora - Ana
- Oscar - Felipe
- Rosa - Paula

La red sigue siendo no dirigida, no hay duplicados, no hay auto-conexiones, existe una ruta alternativa por el ciclo Laura-Mateo-Nora-Oscar-Paula-Juan y Rosa tiene una unica conexion.

Pares seleccionados para ejecutar en `main.py`:

- Laura -> Felipe
- Rosa -> Ana
- Juan -> Karen

## Punto 11. Mejora del sistema

Mejora seleccionada: identificacion de componentes desconectados.

Justificacion: permite saber si dos usuarios no pueden conectarse porque pertenecen a partes separadas de la red. Esto ayuda a explicar los resultados negativos del punto 9.

Codigo: funcion `componentes_conectados` en `busquedas.py`.

Evidencia: `main.py` imprime cada componente encontrado.

