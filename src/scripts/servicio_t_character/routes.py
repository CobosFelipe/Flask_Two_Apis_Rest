""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers


servicio_t_character = Blueprint(
    "servicio_t_character",
    __name__,
    url_prefix="/rym",
)
# Servicios para Metodos GET
servicio_t_character.add_url_rule(
    "/get",
    view_func=controllers.get_characters,
    methods=["GET"]
)
servicio_t_character.add_url_rule(
    "/get/<int:id_character>",
    view_func=controllers.get_characters_by_id,
    methods=["GET"]
)
servicio_t_character.add_url_rule(
    "/get/<name_character>",
    view_func=controllers.get_characters_by_name,
    methods=["GET"]
)
# Servicios para Metodos POST
servicio_t_character.add_url_rule(
    "/post",
    view_func=controllers.add_characters,
    methods=["POST"]
)
# Servicios para Metodos PUT
servicio_t_character.add_url_rule(
    "/put/<int:id_character>",
    view_func=controllers.edit_character,
    methods=["PUT"]
)

