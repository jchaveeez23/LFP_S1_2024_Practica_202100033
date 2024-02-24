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
        elif instruccion[0] == "Dar_de_Comer":
            ar1 = instruccion[1].split(",")
            nick = ar1[0].strip('"')
            for animal in pets:
                if animal.nombre == nick:
                    if pets_result != " ":
                        pets_result = pets_result + animal.Comer(int(ar1[1])) + "\n"
                    else:
                        pets_result = pets_result +  animal.comer(int(ar1[1])) + "\n" 
        elif instruccion[0] == "Resumen_Mascota":
            ar1 = instruccion[1].split(",")
            nick = ar1[0].strip('"')
            for animal in pets:
                if animal.nombre == nick:
                    if pets_result != " ":
                        pets_result = pets_result + animal.Resumen() + "\n"
                    else:
                        pets_result = pets_result + animal.Resumen() + "\n"
        elif linea == "Resumen Global":
            fecha = datetime.datetime.now()
            if pets_result != " ":
                pets_result = pets_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + "----------------- Resumen global -----------------\n"
            else:
                pets_result = "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + "----------------- Resumen global -----------------"

            for animal in pets:
                if pets_result != " ":
                    pets_result = pets_result + animal.Resumen() + "\n"
                else:
                    pets_result = pets_result + animal.F() + "\n"
            pets_result = pets_result + "[%s/%s/%s"%(fecha.day,fecha.month,fecha.year) + " %s:%s"%(fecha.hour,fecha.minute)+"] " + "--------------------------------------------------\n"
    #Creacion de archivo
    resultado = open("C:/Users/cokei/OneDrive/Escritorio/archivo.petworld_result","w")
    resultado.write(pets_result)
    resultado.close()
    os.system("C:/Users/cokei/OneDrive/Escritorio/archivo.petworld_result")
    menuPrincipal()

def menuPrincipal():
    os.system("cls")
    print(" ")
    print("------Menu Principal-------")
    print("|                         |")
    print("| 1. Modulo Pet Manager |")
    print("| 0. Salir                |")
    print("|                         |")
    print("---------------------------")
    print(" ")
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                modulopetmanager()
            elif lectura == 0:
                print("Hasta la proxima c:")
                exit(0)
            else:
                print("\nIngrese una opcion valida\n")
        else:
            print("\nIngrese una opcion valida \n")

def modulopetmanager():
    os.system("cls")
    print(" ")
    print("-------Modulo Pet Manager-------")
    print("|                                |")
    print("| 1. Carga del archivo .petmanager |")
    print("| 0. Regresar al menu principal  |")
    print("|                                |")
    print("----------------------------------")
    print(" ")
    while True:
        lectura = input('Presione el numero de la accion a realizar: ')
        if lectura.isdigit() == True:
            lectura = int(lectura)
            if lectura == 1:
                PetManager()
            elif lectura == 0:
                menuPrincipal()
            else:
                print("\nIngrese una opcion valida \n")
        else:
            print("\nIngrese una opcion valida \n")
