"""Implementaciones de BFS y DFS para buscar conexiones en una red social."""

from collections import deque


def reconstruir_ruta(padres, destino):
    ruta = []
    actual = destino
    while actual is not None:
        ruta.append(actual)
        actual = padres[actual]
    ruta.reverse()
    return ruta


def _resultado_no_existe():
    return {
        "encontrado": False,
        "mensaje": "El usuario no existe en la red.",
        "ruta": [],
        "grados_separacion": None,
        "orden_expansion": [],
        "nodos_expandidos": 0,
        "nodos_generados": 0,
        "frontera_maxima": 0,
    }


def _resultado_sin_conexion(orden_expansion, nodos_generados, frontera_maxima):
    return {
        "encontrado": False,
        "mensaje": "No existe conexion entre los usuarios.",
        "ruta": [],
        "grados_separacion": None,
        "orden_expansion": orden_expansion,
        "nodos_expandidos": len(orden_expansion),
        "nodos_generados": nodos_generados,
        "frontera_maxima": frontera_maxima,
    }


def buscar_conexion_bfs(red, origen, destino):
    if origen not in red or destino not in red:
        return _resultado_no_existe()

    frontera = deque([origen])
    visitados = {origen}
    padres = {origen: None}
    orden_expansion = []
    nodos_generados = 1
    frontera_maxima = 1

    while frontera:
        actual = frontera.popleft()
        orden_expansion.append(actual)

        if actual == destino:
            ruta = reconstruir_ruta(padres, destino)
            return {
                "encontrado": True,
                "ruta": ruta,
                "grados_separacion": len(ruta) - 1,
                "orden_expansion": orden_expansion,
                "nodos_expandidos": len(orden_expansion),
                "nodos_generados": nodos_generados,
                "frontera_maxima": frontera_maxima,
            }

        for vecino in red[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                frontera.append(vecino)
                nodos_generados += 1

        frontera_maxima = max(frontera_maxima, len(frontera))

    return _resultado_sin_conexion(
        orden_expansion,
        nodos_generados,
        frontera_maxima,
    )


def buscar_conexion_dfs(red, origen, destino, limite_profundidad=10):
    if origen not in red or destino not in red:
        return _resultado_no_existe()

    frontera = [(origen, 0)]
    visitados = set()
    padres = {origen: None}
    orden_expansion = []
    nodos_generados = 1
    frontera_maxima = 1

    while frontera:
        actual, profundidad = frontera.pop()

        if actual in visitados:
            continue

        visitados.add(actual)
        orden_expansion.append(actual)

        if actual == destino:
            ruta = reconstruir_ruta(padres, destino)
            return {
                "encontrado": True,
                "ruta": ruta,
                "grados_separacion": len(ruta) - 1,
                "orden_expansion": orden_expansion,
                "nodos_expandidos": len(orden_expansion),
                "nodos_generados": nodos_generados,
                "frontera_maxima": frontera_maxima,
            }

        if profundidad >= limite_profundidad:
            continue

        for vecino in red[actual]:
            if vecino not in visitados:
                if vecino not in padres:
                    padres[vecino] = actual
                frontera.append((vecino, profundidad + 1))
                nodos_generados += 1

        frontera_maxima = max(frontera_maxima, len(frontera))

    return _resultado_sin_conexion(
        orden_expansion,
        nodos_generados,
        frontera_maxima,
    )


def componentes_conectados(red):
    """Mejora punto 11: identifica componentes desconectados con BFS."""
    visitados = set()
    componentes = []

    for origen in red:
        if origen in visitados:
            continue

        componente = []
        cola = deque([origen])
        visitados.add(origen)

        while cola:
            actual = cola.popleft()
            componente.append(actual)
            for vecino in red[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        componentes.append(componente)

    return componentes

