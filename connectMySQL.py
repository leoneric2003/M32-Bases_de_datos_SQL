import mysql.connector
from mysql.connector import Error

def create_connection():
    """Crea una conexión con la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host='195.179.238.58',          # Cambia esto por la dirección de tu servidor MySQL
            user='u927419088_admin',         # Cambia esto por tu usuario de MySQL
            password='#Admin12345#',   # Cambia esto por tu contraseña de MySQL
            database='u927419088_testing_sql' # Cambia esto por el nombre de tu base de datos
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            return connection

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def close_connection(connection):
    """Cierra la conexión con la base de datos MySQL."""
    if connection.is_connected():
        connection.close()
        print("Conexión cerrada")

# Ejemplo de uso
if __name__ == "__main__":
    conn = create_connection()
    # Aquí puedes realizar operaciones con la base de datos, por ejemplo, consultar datos.
    close_connection(conn)
