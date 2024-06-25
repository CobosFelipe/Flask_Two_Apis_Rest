""" Controladores del servicio 1 """

from flask import request
import psycopg2

from .queries import Query
from .clase_t_character import Clase_t_character

class ClasePokemon:
    """ Clase ejemplo """

    def __init__(self, id_character, name, status, gender, species) -> None:
        pass
    
    datos_organizados = {
        "habilidaes": [
            "etc"
        ]
    }

def endpoint_1():
    """Endpoint de ejemplo 1"""
    print("Ejecutano controlador")

    if not ("id_character" in request.args.keys() or "name" in request.args.keys()):
        return "No se encontraron las llaves necesarias"

    id_character = request.args.get("id_character")
    name = request.args.get("name")
    status = request.get("status")
    gender = request.get("gender")
    species = request.get("species")

    datos_pokemon = ClasePokemon(id_character, name, status, gender, species)

    return datos_pokemon.datos_organizados


def endpoint_2():
    """Endpoint de ejemplo 1"""

    datos_pokemon = Clase_t_character()
    datos_pokemon.validar(request.args)

    return datos_pokemon.datos_organizados

def get_characters():
    try:
        results = Query().search_character()
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def add_characters():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().add_character(entrada.get("id_character"), entrada.get("name"), entrada.get("status"), entrada.get("gender"), entrada.get("species"))
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }


def crud_pokemones():
    if request.method == "GET":
        return get_characters()
    if request.method == "POST":
        return add_characters()