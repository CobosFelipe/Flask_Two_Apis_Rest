""" Ejemplo clase ejercicio """

class NotFoundArgs(Exception):
    """ Excepcion customizada para informar la falta de parametros """

class Clase_t_character:
    """ Clase de ejemplo """
    def __init__(self) -> None:
        self.id_character = None
        self.character_name = None
        self.status = None
        self.gender = None
        self.species = None


    def validar(self, args):
        """ funcion para validar las entradas del controlador """

        if not "id_character" in args:
            raise NotFoundArgs("No se ha encontrado el id del personaje en las entradas")
        if not "name" in args:
            raise NotFoundArgs("No se ha encontrado el nombre del personaje en las entradas")

        self.id_character = args["id_character"]
        self.name = args["name"]
