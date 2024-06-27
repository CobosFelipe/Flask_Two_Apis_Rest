""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """
    # Metodos GET
    def search_episode(self, limit, offset):

        query = """
            SELECT * FROM t_episodes ORDER BY id_episode ASC OFFSET %s LIMIT %s
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

            
    def search_episode_by_id(self, id_episode):

        query = """
            SELECT * FROM t_episodes WHERE id_episode = %s
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [id_episode])

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
            
    def search_episode_by_name(self, name):

        primer_nombre = name.split()[0]

        query = """
            SELECT * FROM t_episodes WHERE name_episode LIKE %s
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
    def add_episode(self, id_episode: int, name_episode: str, episode: str):
        query = """
            INSERT INTO t_episodes
            (id_episode, name_episode, episode)
            VALUES(%s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query, [id_episode, name_episode, episode]).decode())
                cursor.execute(query, [id_episode, name_episode, episode])

    # Metodo PUT
    def edit_episode(self, id_episode: str, name_episode: str, episode: str):
        query = """
            UPDATE t_episodes
            SET name_episode=%s, episode=%s
            WHERE id_episode=%s;
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [name_episode, episode, id_episode])

