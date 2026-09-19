# Taller 2 - Busqueda de conexiones en una red social

Implementacion en Python 3 de BFS y DFS para encontrar rutas entre usuarios de una red social representada como grafo no dirigido.

## Archivos

- `red_social.py`: red original, red modificada y validaciones del grafo.
- `busquedas.py`: BFS, DFS, reconstruccion de ruta y mejora de componentes conectados.
- `main.py`: ejecuta las pruebas solicitadas en el taller.
- `datos/red_social.json`: copia de la red base en formato JSON.
- `informe.md`: respuestas y explicacion punto por punto.

## Como ejecutar

Desde esta carpeta:

```bash
python main.py
```

En Windows, si `python` no esta disponible pero si el lanzador de Python:

```bash
py main.py
```

El programa imprime:

1. vecinos y grados de cada usuario;
2. validacion de bidireccionalidad;
3. resultados de BFS y DFS para las seis pruebas;
4. caso sin conexion del punto 9;
5. pruebas con la red modificada del punto 10;
6. mejora del punto 11: componentes conectados.

## Uso directo de las funciones

```python
from busquedas import buscar_conexion_bfs, buscar_conexion_dfs
from red_social import obtener_red_base

red = obtener_red_base()
print(buscar_conexion_bfs(red, "Ana", "Karen"))
print(buscar_conexion_dfs(red, "Ana", "Karen", limite_profundidad=10))
```

Cada busqueda retorna un diccionario con:

- `encontrado`: indica si existe ruta.
- `ruta`: secuencia de usuarios.
- `grados_separacion`: cantidad de aristas en la ruta.
- `orden_expansion`: usuarios extraidos de la frontera.
- `nodos_expandidos`: cantidad de usuarios expandidos.
- `nodos_generados`: cantidad de usuarios agregados a la frontera.
- `frontera_maxima`: tamano maximo de la cola o pila.

