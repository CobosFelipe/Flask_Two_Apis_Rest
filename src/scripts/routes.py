""" Blueprint con todas las rutas de los servicios en el repositorio """

from flask import Blueprint
from src.scripts import logs
from src.scripts.servicio_t_character.routes import servicio_t_character
from src.scripts.servicio_t_pokemon.routes import servicio_t_pokemon

base_blueprint = Blueprint("base_blueprint", __name__)

base_blueprint.register_blueprint(servicio_t_character)
base_blueprint.register_blueprint(servicio_t_pokemon)


## * Registrar logs
base_blueprint.before_app_request(logs.before_app_request)

base_blueprint.after_app_request(logs.after_app_request)

base_blueprint.teardown_app_request(logs.teardown_app_request)
