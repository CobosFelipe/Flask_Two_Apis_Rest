""" Controladores del servicio 1 """

from flask import request
import psycopg2

from .queries import Query
    
# Metodos GET
def get_pokemon():
    try:
        results = Query().search_pokemon()
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

def get_pokemon_by_id(id_pokemon):
    try:
        results = Query().search_pokemon_by_id(id_pokemon)
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

def get_pokemon_by_name(pokemon_name):
    try:
        results = Query().search_pokemon_by_name(pokemon_name)
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

def get_pokemon_by_height(height):
    try:
        results = Query().search_pokemon_by_height(height)
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

def get_pokemon_by_weight(weight):
    try:
        results = Query().search_pokemon_by_weight(weight)
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

# Metodos POST
def add_pokemon():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().add_pokemon(entrada.get("id_pokemon"), entrada.get("pokemon_name"), entrada.get("status"), entrada.get("gender"), entrada.get("species"))
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

def edit_pokemon(id_pokemon):
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().edit_pokemon(id_pokemon, entrada.get("pokemon_name"), entrada.get("status"), entrada.get("gender"), entrada.get("species"))
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
        return get_pokemon()
    if request.method == "POST":
        return add_pokemon()
    if request.method == "PUT":
        return edit_pokemon()