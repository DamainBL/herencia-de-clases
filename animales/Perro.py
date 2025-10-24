from AnimalVM import AnimalVM

class Perro(AnimalVM):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad,"Perro")
        self.raza = (raza)

    def interactuar(self):
        print(f"{self.Nombre} dice: ¡Guau guau!")