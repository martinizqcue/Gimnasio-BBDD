from Aparato import Aparato
from Cliente import Cliente
from Conexion import Conexion
from Recibo import Recibo
from Sesion import Sesion


class GestorGimnasio:
    def __init__(self):
        self.db = Conexion()

    # CRUD para Clientes
    def agregar_cliente(self, id_cliente, nombre):
        try:
            id_cliente = int(id_cliente)
        except ValueError:
            print("Error: La ID del cliente debe ser un número.")
            return

        if any(c.id_cliente == id_cliente for c in self.listar_clientes()):
            print(f"Error: El cliente con ID {id_cliente} ya existe.")
            return

        if not nombre.isalpha() and not all(c.isalpha() or c.isspace() for c in nombre):
            print("Error: El nombre solo debe contener letras.")
            return

        cliente = Cliente(id_cliente, nombre)
        query = "INSERT INTO Clientes (id_cliente, nombre, pago_realizado) VALUES (%s, %s, %s)"
        self.db.ejecutar_query(query, (id_cliente, nombre, cliente.pago_realizado))
        print(f"Cliente {nombre} agregado correctamente.")

    def listar_clientes(self):
        query = "SELECT * FROM Clientes"
        resultados = self.db.obtener_datos(query)

        print("Clientes en la base de datos:")
        for row in resultados:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Pago Realizado: {row[2]}")

        return [Cliente(id_cliente=row[0], nombre=row[1], pago_realizado=row[2]) for row in resultados]

    def eliminar_cliente(self, id_cliente):
        query = "DELETE FROM Clientes WHERE id_cliente = %s"
        self.db.ejecutar_query(query, (id_cliente,))
        print(f"Cliente con ID {id_cliente} eliminado correctamente.")

    def listar_morosos(self):
        query = "SELECT * FROM Clientes WHERE pago_realizado != 'pagado'"
        resultados = self.db.obtener_datos(query)

        if not resultados:
            print("No hay clientes morosos.")
            return []

        morosos = [Cliente(id_cliente=row[0], nombre=row[1], pago_realizado=row[2]) for row in resultados]
        for moroso in morosos:
            print(moroso)

    # CRUD para Aparatos
    def agregar_aparato(self, id_aparato, nombre):
        while True:
            # Verifica si id_aparato es un número
            if not id_aparato.isdigit():
                print("Error: La ID del aparato solo debe contener números.")
                return

            # Convertir id_aparato a entero para comparación
            id_aparato = int(id_aparato)

            # Comprueba si el aparato ya existe
            if any(a.id_aparato == id_aparato for a in self.listar_aparatos()):
                print(f"Error: El aparato con ID {id_aparato} ya existe. Intenta de nuevo.")
                id_aparato = input("Introduce un nuevo ID para el aparato: ")
                continue  # Vuelve a comprobar la nueva ID

            # Verifica que el nombre solo contenga letras
            if not nombre.isalpha() and not all(c.isalpha() or c.isspace() for c in nombre):
                print("Error: El nombre del aparato solo debe contener letras.")
                return

            aparato = Aparato(id_aparato, nombre)
            query = "INSERT INTO Aparatos (id_aparato, nombre) VALUES (%s, %s)"
            self.db.ejecutar_query(query, (id_aparato, nombre))
            print(f"Aparato {nombre} agregado correctamente.")
            break  # Sale del bucle si todo está correcto

    def listar_aparatos(self):
        query = "SELECT * FROM Aparatos"
        resultados = self.db.obtener_datos(query)

        if not resultados:
            print("No hay aparatos en la base de datos.")
            return []

        return [Aparato(id_aparato=row[0], nombre=row[1]) for row in resultados]

    def eliminar_aparato(self, id_aparato):
        query = "DELETE FROM Aparatos WHERE id_aparato = %s"
        self.db.ejecutar_query(query, (id_aparato,))
        print(f"Aparato con ID {id_aparato} eliminado correctamente.")

    # CRUD para Sesiones
    def agregar_sesion(self, id_sesion, dia, hora_str, id_cliente, id_aparato):
        # Verificar si la sesión ya existe
        if any(s.id_sesion == id_sesion for s in self.listar_sesiones()):
            print(f"Error: La sesión con ID {id_sesion} ya existe.")
            return

        # Validar el día
        dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes"]
        if dia.lower() not in dias_validos:
            print(f"Error: El día '{dia}' no es válido. Debe ser un día entre lunes y viernes.")
            return

        # Validar la hora
        try:
            hora_int, minutos_int = map(int, hora_str.split(':'))
            if not (0 <= hora_int <= 23) or minutos_int not in (0, 30):
                print("Error: La hora debe estar en formato HH:MM con minutos 00 o 30.")
                return
        except (ValueError, IndexError):
            print("Error: El formato de hora debe ser HH:MM.")
            return

        # Verificar si el cliente existe directamente en la base de datos
        query_cliente = "SELECT * FROM Clientes WHERE id_cliente = %s"
        cliente_result = self.db.obtener_datos(query_cliente, (id_cliente,))
        if not cliente_result:
            print(f"Error: El cliente con ID {id_cliente} no existe.")
            return

        # Verificar si el aparato existe directamente en la base de datos
        query_aparato = "SELECT * FROM Aparatos WHERE id_aparato = %s"
        aparato_result = self.db.obtener_datos(query_aparato, (id_aparato,))
        if not aparato_result:
            print(f"Error: El aparato con ID {id_aparato} no existe.")
            return

        # Comprobar si ya hay una sesión para ese aparato en ese día y hora
        if any(s.dia == dia and s.hora == hora_str and s.aparato.id_aparato == id_aparato for s in
               self.listar_sesiones()):
            print(f"Error: El aparato con ID {id_aparato} ya está reservado para la hora {hora_str} el {dia}.")
            return

        # Insertar la nueva sesión
        query = "INSERT INTO Sesiones (id_sesion, dia, hora, cliente_id, aparato_id) VALUES (%s, %s, %s, %s, %s)"
        self.db.ejecutar_query(query, (id_sesion, dia, hora_str, id_cliente, id_aparato))
        print(
            f"Sesión creada para el cliente con ID {id_cliente} y aparato con ID {id_aparato} a las {hora_str} el {dia}.")

    def listar_sesiones(self):
        query = """
        SELECT s.id_sesion, s.dia, s.hora, s.cliente_id, c.nombre AS cliente_nombre, 
               s.aparato_id, a.nombre AS aparato_nombre
        FROM Sesiones s 
        JOIN Clientes c ON s.cliente_id = c.id_cliente 
        JOIN Aparatos a ON s.aparato_id = a.id_aparato
        """
        resultados = self.db.obtener_datos(query)

        if not resultados:
            print("No hay sesiones en la base de datos.")
            return []

        return [
            Sesion(
                id_sesion=row[0],
                dia=row[1],
                hora=row[2],
                cliente=Cliente(id_cliente=row[3], nombre=row[4]),  # Nombre del cliente
                aparato=Aparato(id_aparato=row[5], nombre=row[6])  # Nombre del aparato
            )
            for row in resultados
        ]

    def eliminar_sesion(self, id_sesion):
        query = "DELETE FROM Sesiones WHERE id_sesion = %s"
        self.db.ejecutar_query(query, (id_sesion,))
        print(f"Sesión con ID {id_sesion} eliminada correctamente.")

    # CRUD para Recibos
    def generar_recibo(self, id_recibo, id_cliente, mes, mensualidad):
        try:
            id_recibo = int(id_recibo)
        except ValueError:
            print(f"Error: El ID del recibo {id_recibo} debe ser un número válido.")
            return

        # Comprobar si el recibo ya existe
        query = "SELECT * FROM Recibos WHERE id_recibo = %s"
        if self.db.obtener_datos(query, (id_recibo,)):
            print(f"Error: El recibo con ID {id_recibo} ya existe.")
            return

        # Comprobar si el cliente existe
        query_cliente = "SELECT nombre FROM Clientes WHERE id_cliente = %s"
        cliente_data = self.db.obtener_datos(query_cliente, (id_cliente,))
        if not cliente_data:
            print(f"Error: El cliente con ID {id_cliente} no existe.")
            return

        cliente_nombre = cliente_data[0][0]

        # Validar el mes
        try:
            mes_int = int(mes)
            if mes_int < 1 or mes_int > 12:
                print(f"Error: El mes {mes} no es válido. Debe ser un número entre 1 y 12.")
                return
        except ValueError:
            print(f"Error: El mes {mes} debe ser un número válido.")
            return

        # Validar la mensualidad
        try:
            mensualidad_float = float(mensualidad)
            if mensualidad_float <= 0:
                print("Error: La mensualidad debe ser un número positivo.")
                return
        except ValueError:
            print(f"Error: La mensualidad {mensualidad} no es un número válido.")
            return

        # Generar el recibo
        query_insert = "INSERT INTO Recibos (id_recibo, cliente_id, mes, mensualidad) VALUES (%s, %s, %s, %s)"
        self.db.ejecutar_query(query_insert, (id_recibo, id_cliente, mes_int, mensualidad_float))
        print(f"Recibo generado para el cliente {cliente_nombre} de {mensualidad_float} € por el mes {mes_int}.")

    def listar_recibos(self):
        query = "SELECT r.id_recibo, r.cliente_id, r.mes, r.mensualidad, c.nombre FROM Recibos r JOIN Clientes c ON r.cliente_id = c.id_cliente"
        resultados = self.db.obtener_datos(query)

        if not resultados:
            print("No hay recibos en la base de datos.")
            return []

        return [
            Recibo(id_recibo=row[0], cliente=Cliente(id_cliente=row[1], nombre=row[4]), mes=row[2], mensualidad=row[3])
            for row in resultados]

    def registrar_pago(self, id_cliente):
        # Verificamos si el cliente existe directamente en la base de datos
        query = "SELECT nombre FROM Clientes WHERE id_cliente = %s"
        resultado = self.db.obtener_datos(query, (id_cliente,))

        if resultado:
            nombre_cliente = resultado[0][0]
            query = "UPDATE Clientes SET pago_realizado = 'pagado' WHERE id_cliente = %s"
            self.db.ejecutar_query(query, (id_cliente,))
            print(f"Pago registrado para el cliente {nombre_cliente}.")
        else:
            print(f"Error: El cliente con ID {id_cliente} no existe.")



