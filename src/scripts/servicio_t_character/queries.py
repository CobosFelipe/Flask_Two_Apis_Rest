""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """
    # Metodos GET
    def search_character(self):

        query = """
            SELECT * FROM t_character ORDER BY id_character ASC
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_characters = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_characters)

                return objeto_characters
            
    def search_character_by_id(self, id_character):

        query = """
            SELECT * FROM t_character WHERE id_character = %s
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [id_character])

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_characters = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_characters)

                return objeto_characters
            
    def search_character_by_name(self, name_character):

        primer_nombre = name_character.split()[0]

        query = """
            SELECT * FROM t_character WHERE name_character LIKE %s
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [primer_nombre])

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_characters = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_characters)

                return objeto_characters
            
    def search_character_by_gender(self, gender):

        query = """
            SELECT * FROM t_character WHERE gender = %s ORDER BY id_character ASC
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [gender])

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_characters = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_characters)

                return objeto_characters
            
    def search_character_by_specie(self, specie):

        query = """
            SELECT * FROM t_character WHERE species = %s ORDER BY id_character ASC
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [specie])

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_characters = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_characters)

                return objeto_characters

    # Metodo POST
    def add_character(self, id_character: int, name_character: str, status: bool, gender: str, species: str):
        query = """
            INSERT INTO t_character
            (id_character, name_character, status, gender, species)
            VALUES(%s, %s, %s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query, [id_character, name_character, status, gender, species]).decode())
                cursor.execute(query, [id_character, name_character, status, gender, species])

    # Metodo PUT
    def edit_character(self, id_character: str, name_character: str, status: bool, gender: str, species: str):
        query = """
            UPDATE t_character
            SET name_character=%s, status=%s, gender=%s, species=%s
            WHERE id_character=%s;
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [name_character, status, gender, species, id_character])

