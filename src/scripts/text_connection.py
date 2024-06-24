from connection import DBConnection
from psycopg2.extras import RealDictCursor

def test_connection():
    db = DBConnection()
    with db.open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM pokemon")
            result = cursor.fetchone()
            print("Conexión exitosa, resultado de la consulta de prueba:", result)

if _name_ == "_main_":
    test_connection()