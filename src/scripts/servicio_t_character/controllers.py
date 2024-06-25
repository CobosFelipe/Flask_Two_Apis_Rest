""" Controladores del servicio 1 """

from flask import request
import psycopg2

from .queries import Query
from .clase_t_character import Clase_t_character

class ClasePokemon:
    """ Clase ejemplo """

    def __init__(self, id_character, name, status, gender, species) -> None:
        pass
    

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
        Query().add_character(entrada.get("id_character"), entrada.get("name_character"), entrada.get("status"), entrada.get("gender"), entrada.get("species"))
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

def edit_character(id_character):
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().edit_character(id_character, entrada.get("name_character"), entrada.get("status"), entrada.get("gender"), entrada.get("species"))
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
        "msg": "Se modificó satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }


def crud_pokemones():
    if request.method == "GET":
        return get_characters()
    if request.method == "POST":
        return add_characters()