""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers

servicio_t_episodes = Blueprint(
    "servicio_t_episodes",
    __name__,
    url_prefix="/epi",
)
# Servicios para Metodos GET
servicio_t_episodes.add_url_rule(
    "/get",
    view_func=controllers.get_episode,
    methods=["GET"]
)
servicio_t_episodes.add_url_rule(
    "/get/<int:id_episode>",
    view_func=controllers.get_episode_by_id,
    methods=["GET"]
)
servicio_t_episodes.add_url_rule(
    "/get/by_name/<name>",
    view_func=controllers.get_episode_by_name,
    methods=["GET"]
)
# Servicios para Metodos POST
servicio_t_episodes.add_url_rule(
    "/post",
    view_func=controllers.add_episode,
    methods=["POST"]
)
# Servicios para Metodos PUT
servicio_t_episodes.add_url_rule(
    "/put/<int:id_episode>",
    view_func=controllers.edit_episode,
    methods=["PUT"]
)

