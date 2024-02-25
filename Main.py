from Gato import PetManager


print('---------------------------------------')
print('LENGUAJES FORMALES Y DE PROGRAMACION B-')
print('JOSUE DANIEL CHAVEZ PORTILLO')
print('CARNÉ: 202100033')
print('---------------------------------------')
print('')
print('---------------------------------------')
print('PRESIONE ENTER PARA CONTINUAR...')
print('---------------------------------------')
input()


def menu_principal():
    print("MENU PRINCIPAL")
    print("1. Modulo Pet Manager")
    print("2. Salir")

def submenu_pet_manager():
    print("\nModulo PET MANAGER")
    print("1. Cargar Archivo")
    print("2. Salir")

def main():
    gestor_mascotas = PetManager()
    
    while True:
        menu_principal()
        opcion_principal = input("Seleccione una opción: ")
        
        if opcion_principal == "1":
            while True:
                submenu_pet_manager()
                opcion_sub = input("Seleccione una opción: ")
                
                if opcion_sub == "1":
                    nombre_archivo = input("Ingrese el nombre del archivo a cargar: ")
                    gestor_mascotas.cargar_desde_archivo(nombre_archivo)
                elif opcion_sub == "2":
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
        elif opcion_principal == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()