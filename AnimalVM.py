class AnimalVM:
    def __init__(self, Nombre, edad, especie):
        self.Nombre = (Nombre)
        self.especie = (especie)    
        self.edad = (edad)

    def moverse(self):
        return f"{self.Nombre} Camina en 4 patas."

    def informacion(self):
        return f"{self.Nombre} tiene {self.edad} años y es un {self.especie}."