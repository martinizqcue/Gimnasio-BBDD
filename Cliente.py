
class Cliente:
    def __init__(self, id_cliente, nombre, pago_realizado="no pagado"):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.pago_realizado = pago_realizado

    def __str__(self):
        return f"Cliente(ID: {self.id_cliente}, Nombre: {self.nombre})"