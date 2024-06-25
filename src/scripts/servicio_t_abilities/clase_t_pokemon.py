""" Ejemplo clase ejercicio """

class NotFoundArgs(Exception):
    """ Excepcion customizada para informar la falta de parametros """

class Clase_t_abilities:
    """ Clase de ejemplo """
    def __init__(self) -> None:
        self.id_pokemon = None
        self.pokemon_name = None
        self.height = None
        self.weight = None
        self.abilities = None
        self.id_character = None


    def validar(self, args):
        """ funcion para validar las entradas del controlador """

        if not "id_ability" in args:
            raise NotFoundArgs("No se ha encontrado el id de la habilidad en las entradas")
        if not "name" in args:
            raise NotFoundArgs("No se ha encontrado el nombre de la habilidad en las entradas")

        self.id_character = args["id_character"]
        self.name = args["name"]
