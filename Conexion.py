import mysql.connector

class Conexion:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gimnasio_db",
                port="3306",
            )
            print("Conexión exitosa")
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conexion = None  # Asegúrate de que `conexion` sea None si falla
            self.cursor = None  # También aseguramos que `cursor` sea None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()

    def ejecutar_query(self, query, params=None):
        if self.cursor:  # Verifica si `cursor` no es None
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conexion.commit()

    def obtener_datos(self, query, params=None):
        if self.cursor:  # Verifica si `cursor` no es None
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        return []  # Devuelve una lista vacía si no hay cursor
