# Manual Tecnico
# Practica 1
# Primer Semestre 2024
```js
Universidad San Carlos de Guatemala
Estudiante: Josue Daniel Chavez Portillo
Carne: 202100033
```
## 1. Interfaz de Consola
Se programaron inicialmente dos funciones:
"menu_principal" y "submenu_pet_manager", que muestran las opciones que cada menu tiene para poder ejecutar.
![menus](https://i.ibb.co/3WKwkvn/menus.png)

Asi mismo, para la interfaz de la consola se empleo una funcion "main" que es la que utiliza un ciclo while, para poder ejecutar las dos funciones anteriores hasta su interrupcion.
![main](https://i.ibb.co/xDHJ8F3/main.png)

## 2. Clase Gato
Se elaboró una clase llamada Gato, la cual contiene las funciones basicas para que el gato que se cree, ejecute correctamente las acciones correspondientes. Estas son las Siguientes:
### Funcion Constructor
La funcion encargada de tener los parametros iniciales para la creacion del gato.

![constru](https://i.ibb.co/NxGWKX1/ctr2.png)
### Funcion comer
Funcion encargada de realizar la operacion en la cual el gato obtiene energia.
![comer](https://i.ibb.co/sFDKZSH/comer.png)
### Funcion jugar
Funcion encargada de realizar la operacion en la cual el gato pierde energia.
![jugar](https://i.ibb.co/3TpHpxm/jugar.png)

## 3. Clase PetManager
Es la clase que contiene todas las funciones que son necesarias para que el modulo "Pet Manager" pueda funcionar correctamente. Las Funciones son las Siguientes:
### Funcion Constructor
Funcion que contiene la lista en la cual se guardan las mascotas creadas.

![lista](https://i.ibb.co/P6fBB7t/lista.png)
### Funcion crear_gato
Funcion la cual guarda en la lista creada anteriormente el nombre del gato que recibe de el archivo cargado.
![crear](https://i.ibb.co/4ZKQfY3/crear.png)
### Funcion dar_de_comer
Funcion la cual de de comer al gato aumentando su energia dependiendo el peso del raton que comio mas un dato preestablecido de 12.
![eat](https://i.ibb.co/93sFC95/dardecomer.png)
### Funcion jugar
Funcion la cual resta energia al gato dependiendo la cantidad de minutos jugados.
![play](https://i.ibb.co/G7fkk89/juego.png)
### Funcion cargar_desde_archivo
Funcion la cual se encarga de leer y analizar por lineas el archivo .petmanager que se carga en el programa.
![load](https://i.ibb.co/wM1Td5V/carga.png)
### Funcion resumen_mascota
Funcion la cual se encarga de mostrar en consola el estado y la energia total de cada una de las mascotas que contiene el archivo cargado.SS
![resumen](https://i.ibb.co/fDpqn9J/resumenmasco.png)
### Funcion resumen_global
Funcion la cual crea una grafica por medio de la libreria graphviz y muestra todas las mascotas con su respectiva energia y estado en el que se encuentran dentro de dicha grafica.
![resumen](https://i.ibb.co/ws5WqqF/global.png)
### Funcion guardar_resumen_en_archivo
Funcion la cual se encarga de escribir en un archivo .petworld_result, el resumen de las acciones de las mascotas individualmente es deci, un archiv para cada mascota que esta en el archivo.
![resumen](https://i.ibb.co/0KvSPJF/save.png)
### Funcion ejecutar_instruccion
Funcion la cual es la responsable de que se ejecuten las funciones anteriores por medio de la escritura en la que viene las instrucciones de el archivo que se carga en el programa.
![resumen](https://i.ibb.co/G9h49Jq/ejecucion.png)

