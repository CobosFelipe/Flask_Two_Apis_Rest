""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """
    # Metodos GET
    def search_pokemon(self, limit, offset):

        query = """
            SELECT * FROM t_pokemon ORDER BY id_pokemon ASC OFFSET %s LIMIT %s 
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

            
    def search_pokemon_by_id(self, id_pokemon):

        query = """
            SELECT * FROM t_pokemon WHERE id_pokemon = %s
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [id_pokemon])

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
            
    def search_pokemon_by_name(self, pokemon_name):

        primer_nombre = pokemon_name.split()[0]

        query = """
            SELECT * FROM t_pokemon WHERE pokemon_name LIKE %s
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
            
    def search_pokemon_by_height(self, height):

        query = """
            SELECT * FROM t_pokemon WHERE height = %s ORDER BY id_pokemon ASC
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [height])

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
            
    def search_pokemon_by_weight(self, weight):

        query = """
            SELECT * FROM t_pokemon WHERE weight = %s ORDER BY id_pokemon ASC
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [weight])

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
    def add_pokemon(self, id_pokemon: int, pokemon_name: str, height: int, weight: int, abilities: int, id_character: int):
        query = """
            INSERT INTO t_pokemon
            (id_pokemon, pokemon_name, height, weight, abilities, id_character)
            VALUES(%s, %s, %s, %s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query, [id_pokemon, pokemon_name, height, weight, abilities, id_character]).decode())
                cursor.execute(query, [id_pokemon, pokemon_name, height, weight, abilities, id_character])

    # Metodo PUT
    def edit_pokemon(self, id_pokemon: str, pokemon_name: str, height: int, weight: int, abilities: int, id_character: int):
        query = """
            UPDATE t_pokemon
            SET pokemon_name=%s, height=%s, weight=%s, abilities=%s, id_character=%s
            WHERE id_pokemon=%s;
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [pokemon_name, height, weight, abilities, id_character, id_pokemon])

