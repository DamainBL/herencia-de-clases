from animales.Oso import Oso
from animales.gato import Gato
from animales.Perro import Perro
from firebase.firebase_config import initialize_firebase, add_animal_object, get_all_animals

def surbir_animales(animales):

    print("-" * 40)
    for animal in animales:
        print(animal.informacion())
        print(animal.moverse())
        hablar = animal.interactuar()
        if hablar is not None:
            print(hablar)
        key = add_animal_object(animal)
        print("Subido", key ," a la base de datos.")
        print("-" * 40)

def listar_animales():

    data = get_all_animals()

    if data:
        print("\n=== Información obtenida desde la nube ===\n")
        for nombre, info in data.items():
            print(f"{nombre}:")
            for clave, valor in (info or {}).items():
                print(f"   {clave}: {valor}")
            print("-" * 40)


def main():

    perro = Perro("jordano", 53, "pastor aleman")
    gato = Gato("pizarra", 91,   "siames")
    oso = Oso("baloo", 20, "pardo")
    
    animales=[perro, gato, oso]

    initialize_firebase()

    surbir_animales(animales)

    listar_animales()   

    
if __name__ == "__main__":
        main()