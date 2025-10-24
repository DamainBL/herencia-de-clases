# herencia-de-clases

Este proyecto demuestra cómo crear y gestionar objetos de animales en Python, para luego almacenar su información en **Firebase Realtime Database**.

##  Descripción

El sistema define una clase base `AnimalVM` y varias subclases (`Perro`, `Gato`, `Oso`) que heredan su comportamiento.  
Cada animal tiene atributos como **nombre**, **edad**, **raza** y **especie**, y puede realizar acciones simples como moverse o interactuar.

El módulo de Firebase se encarga de:
- Inicializar la conexión con Firebase.
- Convertir los objetos en diccionarios.
- Subirlos y obtenerlos desde la base de datos.

##El programa mostrará en consola:

La información de cada animal.

Las acciones que realiza.

El resultado de la subida a la base de datos.

Los datos recuperados desde Firebase.

##📂 Estructura del Proyecto
.

├── animales/

│   ├── Perro.py

│   ├── Gato.py

│   ├── Oso.py

├── firebase/

│   └── firebase_config.py

├── AnimalVM.py

├── main.py

└── README.md

##Ejemplo de salida


-pizarra tiene 91 años y es un Gato

-pizarra Camina en 4 patas

-pizarra dice: ¡Miau Miau!

-Subido pizarra  a la base de datos


-pizarra:

   -edad: 91
	
   -especie: Gato
	
   -nombre: pizarra
	
   -raza: siames

