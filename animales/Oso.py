from AnimalVM import AnimalVM

class Oso(AnimalVM):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "oso")
        self.raza = (raza)

    def interactuar(self):
        print(f"{self.Nombre} dice: ¡raw raw!")