""" entry point for flask app """

from src.settings import application
from src.scripts.routes import base_blueprint
from src.scripts.routes import servicio_t_character
from src.scripts.routes import servicio_t_pokemon
from src.scripts.routes import servicio_t_abilities

application.register_blueprint(base_blueprint)
application.register_blueprint(servicio_t_character)
application.register_blueprint(servicio_t_pokemon)
application.register_blueprint(servicio_t_abilities)

if __name__ == '__main__':
    application.run()
