""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers


servicio_1_blueprint = Blueprint(
    "servicio_1_blueprint",
    __name__,
    url_prefix='/servicio-1',
)

servicio_1_blueprint.add_url_rule(
    "/ejemplo",
    view_func=controllers.endpoint_1,
    methods=["GET"]
)
servicio_1_blueprint.add_url_rule(
    "/ejemplo-body",
    view_func=controllers.endpoint_2,
    methods=["POST"]
)
