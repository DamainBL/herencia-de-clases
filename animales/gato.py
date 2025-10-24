from AnimalVM import AnimalVM

class Gato(AnimalVM):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Gato")
        self.raza = (raza)

    def interactuar(self):
        print(f"{self.Nombre} dice: ¡Miau Miau!")