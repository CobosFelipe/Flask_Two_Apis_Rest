""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers


servicio_t_character = Blueprint(
    "servicio_t_character",
    __name__,
    url_prefix="/rym",
)

servicio_t_character.add_url_rule(
    "/get",
    view_func=controllers.get_characters,
    methods=["GET"]
)
servicio_t_character.add_url_rule(
    "/post",
    view_func=controllers.add_characters,
    methods=["POST"]
)
servicio_t_character.add_url_rule(
    "/put/<int:id_character>",
    view_func=controllers.edit_character,
    methods=["PUT"]
)

