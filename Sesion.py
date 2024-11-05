class Sesion:
    def __init__(self, id_sesion, dia, hora, cliente, aparato):
        self.id_sesion = id_sesion
        self.dia = dia
        self.hora = hora
        self.cliente = cliente
        self.aparato = aparato

    def __str__(self):
        return f"Sesion(ID: {self.id_sesion}, Dia: {self.dia}, Hora: {self.hora}, Cliente: {self.cliente.nombre}, Aparato: {self.aparato.nombre})"
