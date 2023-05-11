import random
import datetime
from verificaciones import verificar_ingreso_y_numero

def logica_batalla(lista):
    '''
    se encarga de la mayor parte de la logica del archivo, desde buscar a los personajes hasta compararlos y determinar al ganador

    parametros:
    lista: lista original de la cual se sacan los personajes

    retorno: mensaje
    '''
    usuario = input("Ingresa la ID del personaje que quieras elegir (del 1 al 35) ")
    usuario = verificar_ingreso_y_numero(usuario)
    maquina = numero_aleatorio()
    lista_usuario = buscar_guardar_por_id(lista, 'id', 'nombre', 'poder_ataque', usuario)
    lista_maquina = buscar_guardar_por_id(lista, 'id', 'nombre', 'poder_ataque', maquina)
    fecha = fecha_arreglada()
    if lista_usuario[1] > lista_maquina[1]:
        msj = (f"Gano el usuario con {lista_usuario[0]} a {lista_maquina[0]}, Fecha: {fecha}\n")
    else:
        msj = (f"Gano la maquina con {lista_maquina[0]} a {lista_usuario[0]}, Fecha: {fecha}\n")
    return msj

def numero_aleatorio():
    '''
    crea y retorna un numero aleatorio

    retorno: numero aleatorio
    '''
    return random.randint(1, 36)

def batalla_principal(lista):
    '''
    se encarga de la ejecucion de al funcion del archivo

    parametros:
    lista: lista necesaria para los archivos
    '''
    msj = logica_batalla(lista)
    agregar_al_archivo_de_texto(msj)

def buscar_guardar_por_id(lista ,key_busqueda, key_guardar, key_guardar_int, dato_comparar):
    '''
    se encarga de buscar, comparar y guardar datos de una lista

    parametros:
    lista:
    key_busqueda: key de diccionario a comparar
    key_guardar: key de diccionario a guardar (str)
    key_guardar_int: key de diccionario a guardar (int)
    dato_comparar: dato con el que se compara key busqueda
    '''
    lista_retorno = []
    for pj in lista:
        if int(pj[key_busqueda]) == int(dato_comparar):
            pj_nombre = pj[key_guardar]
            lista_retorno.append(pj_nombre)
            poder = int(pj[key_guardar_int])
            lista_retorno.append(poder)
    return lista_retorno

def guardar_fecha_y_hora():
    '''
    se encarga de guardar la fecha y hora actual

    retorno: retorna una lista con el año-mes-dia actuales
    '''
    horario = []
    fecha_hora_actual = datetime.datetime.now()
    año_actual = fecha_hora_actual.year
    mes_actual = fecha_hora_actual.month
    dia_actual = fecha_hora_actual.day
    horario.extend([año_actual, mes_actual, dia_actual])
    return horario

def join(lista, conector):
    '''
    une una lista con un conector

    parametros:
    lista: lista a unir
    conector: valor con el que se une la lista

    retorno: retorna un string
    '''
    cadena = conector.join(lista)
    return cadena

def fecha_arreglada():
    '''
    se encarga de arreglar el formato de la fecha

    retorno: retorna la fecha en el formato correcto para su uso
    '''
    horario = guardar_fecha_y_hora()
    lista_arreglada = arreglar_lista_fecha(horario)
    final = join(lista_arreglada, "/")
    return final

def arreglar_lista_fecha(lista):
    '''
    se encarga de transformar los datos numericos de una lista en string

    parametros:
    lista: lista con la fecha

    retorno: retorna la lista arreglada con todos los valores en string
    '''
    lista_arreglada = []
    for X in lista:
        valor = str(X)
        lista_arreglada.append(valor)
    return lista_arreglada

def agregar_al_archivo_de_texto(msj):
    '''
    se encarga de agregar el mensaje al archivo de texto

    parametros:
    msj: mensaje a agregar
    '''
    with open('C:\\Users\\User\\OneDrive\\Escritorio\\Cosas UTN\\1er Cuatri\\Python\\Parcial\\resultado_batalla.txt', mode='a', encoding="utf-8") as archivo:
        archivo.write(msj)
    archivo.close()
