from firebase_admin import credentials, db
import firebase_admin

def initialize_firebase():

    cred = credentials.Certificate("")
    firebase_admin.initialize_app(cred, {'databaseURL': ''})

def animal_to_dict(animal):

    nombre = getattr(animal, "Nombre")
    edad = getattr(animal, "edad") 
    raza = getattr(animal, "raza") 
    especie = getattr(animal, "especie") 

    return {
        "nombre": nombre,
        "edad": edad,
        "raza": raza,
        "especie": especie
    }

def add_animal_dict(animal_dict):
    nombre = animal_dict.get('nombre')
    ref = db.reference('animals').child(nombre)
    ref.set(animal_dict)
    return ref.key

def add_animal_object(animal):
    data = animal_to_dict(animal)
    return add_animal_dict(data)

def get_all_animals():
    ref = db.reference('animals')
    data = ref.get()
    return data 

