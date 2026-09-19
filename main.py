"""Programa principal del Taller 2: busqueda de conexiones en una red social."""

from busquedas import buscar_conexion_bfs, buscar_conexion_dfs, componentes_conectados
from red_social import (
    obtener_red_base,
    obtener_red_con_componente_separado,
    obtener_red_modificada,
    usuarios_aislados,
    validar_bidireccionalidad,
    vecinos_y_grados,
)


PRUEBAS = [
    ("Ana", "Karen"),
    ("Bruno", "Jorge"),
    ("Diana", "Isabel"),
    ("Gabriel", "Elena"),
    ("Felipe", "Karen"),
    ("Helena", "Ana"),
]

PRUEBAS_MODIFICADAS = [
    ("Laura", "Felipe"),
    ("Rosa", "Ana"),
    ("Juan", "Karen"),
]


def formatear_ruta(resultado):
    if not resultado["encontrado"]:
        return resultado.get("mensaje", "Sin conexion")
    return " -> ".join(resultado["ruta"])


def imprimir_resultado(nombre, resultado):
    print(f"{nombre}")
    print(f"  Encontrado: {resultado['encontrado']}")
    print(f"  Ruta: {formatear_ruta(resultado)}")
    print(f"  Grados: {resultado['grados_separacion']}")
    print(f"  Orden expansion: {resultado['orden_expansion']}")
    print(f"  Expandidos: {resultado['nodos_expandidos']}")
    print(f"  Generados: {resultado['nodos_generados']}")
    print(f"  Frontera maxima: {resultado['frontera_maxima']}")


def ejecutar_pruebas(red, pruebas, titulo):
    print(f"\n{titulo}")
    print("=" * len(titulo))
    for indice, (origen, destino) in enumerate(pruebas, start=1):
        print(f"\nPrueba {indice}: {origen} -> {destino}")
        imprimir_resultado("BFS", buscar_conexion_bfs(red, origen, destino))
        imprimir_resultado("DFS", buscar_conexion_dfs(red, origen, destino))


def mostrar_analisis_grafo(red):
    print("Punto 2: vecinos y grados")
    print("=========================")
    for usuario, datos in vecinos_y_grados(red).items():
        vecinos = ", ".join(datos["vecinos"])
        print(f"{usuario:8} | grado {datos['grado']} | {vecinos}")

    max_grado = max(len(vecinos) for vecinos in red.values())
    usuarios_mas_conectados = [
        usuario for usuario, vecinos in red.items() if len(vecinos) == max_grado
    ]
    print(f"\nMayor grado: {max_grado} ({', '.join(usuarios_mas_conectados)})")
    print(f"Usuarios aislados: {usuarios_aislados(red) or 'Ninguno'}")
    errores = validar_bidireccionalidad(red)
    print(f"Conexiones no bidireccionales: {errores or 'Ninguna'}")


def ejecutar_punto_9():
    red = obtener_red_con_componente_separado()
    print("\nPunto 9: usuarios sin conexion")
    print("==============================")
    imprimir_resultado("BFS Ana -> Laura", buscar_conexion_bfs(red, "Ana", "Laura"))
    imprimir_resultado("DFS Ana -> Laura", buscar_conexion_dfs(red, "Ana", "Laura", 10))
    print(f"Componentes: {componentes_conectados(red)}")


def ejecutar_mejora_componentes(red):
    print("\nPunto 11: mejora - componentes desconectados")
    print("============================================")
    for indice, componente in enumerate(componentes_conectados(red), start=1):
        print(f"Componente {indice}: {', '.join(componente)}")


def main():
    red_base = obtener_red_base()
    mostrar_analisis_grafo(red_base)
    ejecutar_pruebas(red_base, PRUEBAS, "Punto 7: pruebas en la red base")
    ejecutar_punto_9()

    red_modificada = obtener_red_modificada()
    ejecutar_pruebas(red_modificada, PRUEBAS_MODIFICADAS, "Punto 10: red modificada")
    ejecutar_mejora_componentes(red_modificada)


if __name__ == "__main__":
    main()

