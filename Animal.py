class Animal():
    def __init__(self,nombre,energia,estado,tiempo):
        self.nombre = nombre
        self.energia = energia
        self.estado = estado
        self.tiempo = tiempo

    def VerificarEstado(self):
        if self.energia == 0:
            self.estado = False
        else:
            self.estado = True