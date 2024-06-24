""" Controladores del servicio 1 """

from flask import request

from .clase_ejemplo import ClaseEjemplo

class ClasePokemon:
    """ Clase ejemplo """

    def __init__(self, nombre_pokemon, nombre_persona) -> None:
        pass

    datos_organizados = {
        "habilidaes": [
            "etc"
        ]
    }

def endpoint_1():
    """Endpoint de ejemplo 1"""
    print("Ejecutano controlador")

    if not ("nombre_pokemon" in request.args.keys() and "nombre_persona" in request.args.keys()):
        return "No se encontraron las llaves necesarias"

    nombre_pokemon = request.args.get("nombre_pokemon")
    nombre_persona = request.args.get("nombre_persona")

    datos_pokemon = ClasePokemon(nombre_pokemon, nombre_persona)

    return datos_pokemon.datos_organizados


def endpoint_2():
    """Endpoint de ejemplo 1"""

    datos_pokemon = ClaseEjemplo()
    datos_pokemon.validar(request.args)

    return datos_pokemon.datos_organizados
