"""Datos y utilidades para construir la red social del taller."""

from copy import deepcopy


RED_SOCIAL_BASE = {
    "Ana": ["Bruno", "Carla", "Elena"],
    "Bruno": ["Ana", "Diana", "Felipe"],
    "Carla": ["Ana", "Felipe", "Gabriel"],
    "Diana": ["Bruno", "Helena"],
    "Elena": ["Ana", "Isabel"],
    "Felipe": ["Bruno", "Carla", "Helena"],
    "Gabriel": ["Carla", "Jorge"],
    "Helena": ["Diana", "Felipe", "Karen"],
    "Isabel": ["Elena", "Karen"],
    "Jorge": ["Gabriel", "Karen"],
    "Karen": ["Helena", "Isabel", "Jorge"],
}


CONEXIONES_EXTRA = [
    ("Laura", "Mateo"),
    ("Mateo", "Nora"),
    ("Nora", "Oscar"),
    ("Oscar", "Paula"),
    ("Paula", "Juan"),
    ("Juan", "Laura"),
    ("Nora", "Ana"),
    ("Oscar", "Felipe"),
    ("Rosa", "Paula"),
]


def obtener_red_base():
    """Devuelve una copia independiente de la red original."""
    return deepcopy(RED_SOCIAL_BASE)


def agregar_usuario(red, usuario):
    """Agrega un usuario si no existe."""
    red.setdefault(usuario, [])


def agregar_conexion(red, usuario_a, usuario_b):
    """Agrega una conexion no dirigida, sin duplicados ni auto-conexiones."""
    if usuario_a == usuario_b:
        raise ValueError("Un usuario no puede conectarse consigo mismo.")

    agregar_usuario(red, usuario_a)
    agregar_usuario(red, usuario_b)

    if usuario_b not in red[usuario_a]:
        red[usuario_a].append(usuario_b)
    if usuario_a not in red[usuario_b]:
        red[usuario_b].append(usuario_a)


def obtener_red_con_componente_separado():
    """Red del punto 9: Laura y Mateo quedan aislados del componente principal."""
    red = obtener_red_base()
    agregar_conexion(red, "Laura", "Mateo")
    return red


def obtener_red_modificada():
    """Red del punto 10 con cinco usuarios extra y rutas alternativas."""
    red = obtener_red_base()
    for usuario_a, usuario_b in CONEXIONES_EXTRA:
        agregar_conexion(red, usuario_a, usuario_b)
    return red


def vecinos_y_grados(red):
    """Retorna vecinos y grado de cada usuario."""
    return {
        usuario: {
            "vecinos": list(vecinos),
            "grado": len(vecinos),
        }
        for usuario, vecinos in red.items()
    }


def validar_bidireccionalidad(red):
    """Lista conexiones que no tienen su relacion inversa."""
    errores = []
    for usuario, vecinos in red.items():
        for vecino in vecinos:
            if usuario not in red.get(vecino, []):
                errores.append((usuario, vecino))
    return errores


def usuarios_aislados(red):
    """Retorna usuarios sin conexiones."""
    return [usuario for usuario, vecinos in red.items() if not vecinos]

