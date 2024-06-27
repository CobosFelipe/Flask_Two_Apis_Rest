""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """
    # Metodos GET
    def search_ability(self, limit, offset):

        query = """
            SELECT * FROM t_abilities ORDER BY id_ability ASC OFFSET %s LIMIT %s
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [int(offset), int(limit)])

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
                objeto_pokemons = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pokemons)

                return objeto_pokemons

            
    def search_ability_by_id(self, id_ability):

        query = """
            SELECT * FROM t_abilities WHERE id_ability = %s
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [id_ability])

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
                objeto_pokemons = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pokemons)

                return objeto_pokemons
            
    def search_ability_by_name(self, name):

        primer_nombre = name.split()[0]

        query = """
            SELECT * FROM t_abilities WHERE name LIKE %s
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
                objeto_pokemons = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pokemons)

                return objeto_pokemons
            

    # Metodo POST
    def add_ability(self, id_ability: int, name: str):
        query = """
            INSERT INTO t_abilities
            (id_ability, name)
            VALUES(%s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query, [id_ability, name]).decode())
                cursor.execute(query, [id_ability, name])

    # Metodo PUT
    def edit_ability(self, id_ability: str, name: str):
        query = """
            UPDATE t_abilities
            SET name=%s
            WHERE id_ability=%s;
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [name, id_ability])

