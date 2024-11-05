class Aparato:
    def __init__(self, id_aparato, nombre):
        self.id_aparato = id_aparato
        self.nombre = nombre

    def __str__(self):
        return f"Aparato(ID: {self.id_aparato}, Nombre: {self.nombre})"


