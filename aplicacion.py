# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:20:25 2024

@author: JESUS
"""
# Importamos gestion_archivos ESO LO HEMOS CREADO EN OTRO py
import gestion_archivos

# Definimos el menu principal de las opciones y en cada opcion colocamosun mensaje
def menu():
    print("\n ------ BIENVENIDO AL MENU PRINCIPAL ------")
    print("1. Cree su archivo")
    print("2. Escoga el archivo a eliminar")
    print("3. Agregue el contenido")
    print("4. Mostrar el contenido del archivo que hemos creado ")
    print("5. Salir del programa")

# Creamos la opción de crear un archivo

def crear():
    print("\nIngrese su archivo a crear")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_archivos.crear_archivo(archivo, contenido)

# Creamos el método a eliminar, para eliminar algun archivo

def eliminar():    
    print("\nElimine un Archivo")
    archivo = input("Archivo: ")
    gestion_archivos.eliminar_archivo(archivo)

# Agregamos un archivo
def agregar():
    print("\nAgregue datos que Ud desee a un Archivo")
    archivo = input("Archivo: ")
    contenido = input("Contenido: ")
    gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
    
# Listamos los archivos que tenemos

def listar():
    print("\nMostrar los contenidos del archivo que tenemos")
    archivo = input("Archivo: ")
    print(gestion_archivos.leer_archivo(archivo))


# Salimos del programa

def salir():
    print("\nUd salio del programa, Gracias por su visita, vuelva pronto.")

# En caso de una opcion incorrecta, nos dira que dicha opcion es incorrecta

def error():
    print("Opción incorrecta")

# Creamos las opciones a escoger

opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("\nIngrese una opcion: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        print("Opcion ingresada INCORRECTA.")
        error()
        
        