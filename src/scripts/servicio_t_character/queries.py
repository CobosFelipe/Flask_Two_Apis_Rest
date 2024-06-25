""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """

    def search_character(self):
        """
        It does nothing.
        """

        query = """
            SELECT tc.*, te.* FROM t_character tc
	        INNER JOIN union_char_episode uce on tc.id_character = uce.id_character
	        INNER JOIN t_episodes te on uce.id_episode = te.id_episode
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

    def add_character(self, id_character: int, name: str, status: bool, gender: str, species: str):
        query = """
            INSERT INTO t_character
            (id_character, name, status, gender, species)
            VALUES(%s, %s, %s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query, [id_character, name, status, gender, species]).decode())
                cursor.execute(query, [id_character, name, status, gender, species])

