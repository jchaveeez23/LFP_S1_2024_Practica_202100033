import os
import datetime
import time
from Gato import Gato
from Animal import Animal

print(" ")
print("----------Datos del estudiante----------")
print("|                                      |")
print("| Lenguajes formales y de programacion |")
print("|              Seccion: B-             |")
print("|           Carne: 202100033          |")
print("|    Josue Daniel Chavez Portillo     |")
print("----------------------------------------")
print(" ")
input("Presione enter para continuar")

def PetManager():
    path = input("\nIngrese la ruta del archivo: ")
    pets = []
    pets_result = " "

    while True:
        nombre,extension = os.path.splitext(path)
        if extension == '.petmanager':
            break
        else:
            path = input('\nIngrese la ruta del archivo: ')
    
    archivo_pets = open(path,'r')
    contenido = archivo_pets.read()

    division = contenido.split('\n')

    for linea in division:
        instruccion = linea.split(':')
        fecha = datetime.datetime.now()

        if instruccion[0] == 'Crear_Gato':
            nombre = instruccion[1].strip('"')
            g1 = Gato(nombre,1,True,0,0)
            pets.append(g1)

            if pets_result != '':
                pets_result = pets_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Se creo el gato " + nombre +"\n"
            else:
                pets_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] Se creo el gato " + nombre + "\n"
            
