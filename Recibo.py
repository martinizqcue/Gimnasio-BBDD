class Recibo:
    def __init__(self, id_recibo, cliente, mes, mensualidad):
        self.id_recibo = id_recibo
        self.cliente = cliente
        self.mes = mes
        self.mensualidad = mensualidad

    def __str__(self):
        return f"Recibo(ID: {self.id_recibo}, Cliente: {self.cliente.nombre}, Mes: {self.mes}, Mensualidad: {self.mensualidad})"
