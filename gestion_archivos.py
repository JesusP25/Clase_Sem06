# -*- coding: utf-8 -*-
"""
         Trabajo individual de la semana 06 - Lun 06 / 05 / 2024
"""

import os

# Definimos el crear_archivos
def crear_archivo(nombre, contenido):
    archivo = open(nombre,"wt")
    archivo.write(contenido)
    archivo.close()

# Creamos el eliminar_archivo
def eliminar_archivo(nombre):
    os.remove(nombre)

# Creamos el agregar_contenido_archivo
def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()

# Creamos el leer_archivo
def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido
