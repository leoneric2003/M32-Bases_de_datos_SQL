import mysql.connector
import pandas as pd
from mysql.connector import Error

def create_connection():
    """Crea una conexión con la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host='195.179.238.58',  # Cambia esto por la dirección de tu servidor MySQL
            user='u927419088_admin',  # Cambia esto por tu usuario de MySQL
            password='#Admin12345#',  # Cambia esto por tu contraseña de MySQL
            database='u927419088_testing_sql'  # Cambia esto por el nombre de tu base de datos
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def fetch_data(query, connection):
    """Ejecuta una consulta y devuelve los resultados en un DataFrame."""
    try:
        df = pd.read_sql(query, connection)
        return df
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

def export_to_excel(df, file_path):
    """Exporta el DataFrame a un archivo Excel."""
    try:
        df.to_excel(file_path, index=False, engine='openpyxl')
        print(f"Datos exportados exitosamente a {file_path}")
    except Exception as e:
        print(f"Error al exportar a Excel: {e}")

def main():
    # Define tu consulta SQL para obtener asignaturas con 6 créditos
    query = "SELECT * FROM asignatura WHERE creditos = 6;"  # Cambia 'creditos' por el nombre correcto del campo

    # Conectar a la base de datos
    connection = create_connection()

    if connection:
        # Consultar datos
        df = fetch_data(query, connection)

        if df is not None:
            # Exportar a Excel
            export_to_excel(df, 'datos_asignatura_6_creditos.xlsx')

        # Cerrar la conexión
        connection.close()

if __name__ == "__main__":
    main()
