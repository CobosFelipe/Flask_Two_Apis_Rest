""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers


servicio_t_pokemon = Blueprint(
    "servicio_t_pokemon",
    __name__,
    url_prefix="/pok",
)
# Servicios para Metodos GET
servicio_t_pokemon.add_url_rule(
    "/get",
    view_func=controllers.get_pokemon,
    methods=["GET"]
)
servicio_t_pokemon.add_url_rule(
    "/get/<int:id_pokemon>",
    view_func=controllers.get_pokemon_by_id,
    methods=["GET"]
)
servicio_t_pokemon.add_url_rule(
    "/get/by_name/<pokemon_name>",
    view_func=controllers.get_pokemon_by_name,
    methods=["GET"]
)
servicio_t_pokemon.add_url_rule(
    "/get/by_height/<height>",
    view_func=controllers.get_pokemon_by_height,
    methods=["GET"]
)
servicio_t_pokemon.add_url_rule(
    "/get/by_weight/<weight>",
    view_func=controllers.get_pokemon_by_weight,
    methods=["GET"]
)
# Servicios para Metodos POST
servicio_t_pokemon.add_url_rule(
    "/post",
    view_func=controllers.add_pokemon,
    methods=["POST"]
)
# Servicios para Metodos PUT
servicio_t_pokemon.add_url_rule(
    "/put/<int:id_character>",
    view_func=controllers.edit_pokemon,
    methods=["PUT"]
)

