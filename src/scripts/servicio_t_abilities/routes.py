""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers

servicio_t_abilities = Blueprint(
    "servicio_t_abilities",
    __name__,
    url_prefix="/abi",
)
# Servicios para Metodos GET
servicio_t_abilities.add_url_rule(
    "/get",
    view_func=controllers.get_ability,
    methods=["GET"]
)
servicio_t_abilities.add_url_rule(
    "/get/<int:id_ability>",
    view_func=controllers.get_ability_by_id,
    methods=["GET"]
)
servicio_t_abilities.add_url_rule(
    "/get/by_name/<name>",
    view_func=controllers.get_ability_by_name,
    methods=["GET"]
)
# Servicios para Metodos POST
servicio_t_abilities.add_url_rule(
    "/post",
    view_func=controllers.add_ability,
    methods=["POST"]
)
# Servicios para Metodos PUT
servicio_t_abilities.add_url_rule(
    "/put/<int:id_ability>",
    view_func=controllers.edit_ability,
    methods=["PUT"]
)

