from os import system
from ejercicios_listas import *
from ejercicio_batalla import *
from leer_csv import *
from escribir_leer_json import *

menu =[
    "1_ Listar cantidad por raza",
    "2_ Listar personajes por raza",
    "3_ Listar personajes por habilidad",
    "4_ Jugar batalla",
    "5_ Guardar en archivo Json",
    "6_ Leer archivo Json",
    "7_ Salir",
]

def mostrar_menu(lista:list):
    '''
    muestra el menu

    parametro:
    lista: la lista del menu
    '''
    for opcion in lista:
        print(opcion)

def validar_respuesta():
    '''
    pide y valida la respuesta

    retorno: retorna la respuesta o un -1 en caso de que no sea un numero
    '''
    respuesta = input("ingrese una opcion ")
    if validar_entero(respuesta):
        respuesta = int(respuesta)
        return respuesta
    else:
        respuesta = -1
        return respuesta

def validar_entero(X:str):
    '''
    evalua que la respuesta sea un numero

    parametros:
    X: el valor a evaluar

    retorna: verdadero o falso dependiendo de si es o no un numero
    '''
    if X.isdigit():
        return True
    else:
        return False

def sistema_principal():
    '''
    se encarga de la logica del menu, de recibir la respuesta para diriguir al usuario a la funcion deseada
        y de la gestion de las distintas funcoines de los demas archivos 
    '''
    titulo_archivo = "No hay archivo todavia, debes usar la funcion 5 antes"
    lista = obtener_lista_csv("C://Users//User//OneDrive//Escritorio//Cosas UTN//1er Cuatri//Python//Parcial//DBZ.csv")
    while True:
        print(f"\n")
        mostrar_menu(menu)
        print(f"\n")
        respuesta = validar_respuesta()
        print(f"\n")
        match respuesta:
            case -1:
                print("El elemento ingresado no era un numero")
            case 1:
                lista_contador(lista, 'raza')
            case 2:
                personajes_por_tipo(lista, 'raza')
            case 3:
                personajes_por_habilidad(lista)
            case 4:
                batalla_principal(lista)
            case 5:
                titulo_archivo = main_escribir_json(lista)
            case 6:
                if titulo_archivo == "No hay archivo todavia, debes usar la funcion 5 antes":
                    print(titulo_archivo)
                else:
                    leer_json(titulo_archivo)
            case 7:
                system("cls")
                break
            case _:
                print("El numero no es una opcion")
