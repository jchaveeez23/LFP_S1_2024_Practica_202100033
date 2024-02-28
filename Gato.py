import graphviz
class Gato:
    def __init__(self,nombre):
        self.nombre = nombre
        self.energia = 1 
        self.vivo  = True

    def comer(self,peso_raton):
        self.energia += 12 + peso_raton

    def jugar(self,tiempo):
        self.energia -= tiempo * 0.1
        if self.energia <= 0:
            self.vivo = False
        else:
            self.vivo = True
    
#Acciones PetManager

import datetime

class PetManager:
    def __init__(self):
        self.mascotas = {}
    
    def crear_gato(self, nombre):
        self.mascotas[nombre] = Gato(nombre)  

    def dar_de_comer(self, nombre, peso):
        mascota = self.mascotas.get(nombre)
        if mascota:
            mascota.comer(peso) 
        else:
            print("No se encontró la mascota con ese nombre.")

    def jugar(self, nombre, tiempo):
        mascota = self.mascotas.get(nombre)
        if mascota:
            mascota.jugar(tiempo)
        else:
            print("No se encontró la mascota con ese nombre.")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:  
                        partes = linea.split(':')
                        instruccion = partes[0]
                        parametros = partes[1] if len(partes) > 1 else None

                        if instruccion == "Resumen_Global":
                            self.resumen_global()
                        elif parametros:
                            self.ejecutar_instruccion(instruccion, parametros)
                        else:
                            print(f"La línea '{linea}' no tiene el formato esperado y será ignorada.")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar desde archivo: {str(e)}")

    def resumen_mascota(self, nombre):
        mascota = self.mascotas.get(nombre)
        if mascota:
            print(f"[{datetime.datetime.now()}] {nombre}, Energía: {mascota.energia}, Gato, {'Vivo' if mascota.vivo else 'Muerto'}")
            self.guardar_resumen_en_archivo(nombre, f"Energía: {mascota.energia}, {'Vivo' if mascota.vivo else 'Muerto'}")
        else:
            print("No se encontró la mascota con ese nombre.")

    def resumen_global(self):
        dot = graphviz.Digraph(comment='Resumen Global')

        # Agregar nodos para cada mascota con su nombre, energía y estado
        for nombre, mascota in self.mascotas.items():
            dot.node(nombre, f"{nombre}")

            # Conectar nodo de mascota con su estado
            estado = f"Estado_{nombre}"
            dot.node(estado, f"Estado: {'Vivo' if mascota.vivo else 'Muerto'}")
            dot.edge(nombre, estado)

        # Conectar nodos por energía
        for nombre, mascota in self.mascotas.items():
            energia = mascota.energia
            dot.node(str(energia), f"Energía: {energia}")
            dot.edge(nombre, str(energia))

        # Guardar el gráfico en un archivo
        dot.render('resumen_global', format='png', cleanup=True)
        print("Gráfico de resumen global generado correctamente.")

    def guardar_resumen_en_archivo(self, nombre, informacion):
        nombre_archivo = f"{nombre}_resumen.petworld_result"
        try:
            with open(nombre_archivo, 'a') as archivo:
                archivo.write(f"[{datetime.datetime.now()}] {nombre}, {informacion}\n")
            print(f"Resumen guardado en {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar el resumen en el archivo: {str(e)}")

    def ejecutar_instruccion(self, instruccion, parametros):
        try:
            if isinstance(parametros, list):  
                parametros = parametros[0]  
            if instruccion == "Crear_Gato":
                nombre = str(parametros)
                self.crear_gato(nombre.strip())
            elif instruccion == "Dar_de_Comer":
                nombre, peso = str(parametros).split(',')
                self.dar_de_comer(nombre.strip(), int(peso.strip()))
            elif instruccion == "Jugar":
                nombre, tiempo = str(parametros).split(',')
                self.jugar(nombre.strip(), int(tiempo.strip()))
            elif instruccion == "Resumen_Mascota":
                nombre = str(parametros)
                self.resumen_mascota(nombre.strip())
            elif instruccion == "Resumen_Global":
                self.resumen_global()
            else:
                print(f"Instrucción no reconocida: {instruccion}")
        except Exception as e:
            print(f"Error al ejecutar instrucción: {e}")