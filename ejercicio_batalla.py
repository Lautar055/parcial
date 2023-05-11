import random
import datetime

def logica_batalla(lista):
    usuario = input("Ingresa la ID del personaje que quieras elegir (del 1 al 35) ")
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
    return random.randint(1, 36)

def batalla_principal(lista):
    msj = logica_batalla(lista)
    print(msj)
    agregar_al_archivo_de_texto(msj)

def buscar_guardar_por_id(lista ,key_busqueda, key_guardar, key_guardar_int, dato_comparar):
    lista_retorno = []
    for pj in lista:
        if int(pj[key_busqueda]) == int(dato_comparar):
            pj_nombre = pj[key_guardar]
            lista_retorno.append(pj_nombre)
            poder = int(pj[key_guardar_int])
            lista_retorno.append(poder)
    return lista_retorno

def guardar_fecha_y_hora():
    horario = []
    fecha_hora_actual = datetime.datetime.now()
    año_actual = fecha_hora_actual.year
    mes_actual = fecha_hora_actual.month
    dia_actual = fecha_hora_actual.day
    horario.extend([año_actual, mes_actual, dia_actual])
    return horario

def join(lista, conector):
    cadena = conector.join(lista)
    return cadena

def fecha_arreglada():
    horario = guardar_fecha_y_hora()
    lista_arreglada = arreglar_lista_fecha(horario)
    final = join(lista_arreglada, "/")
    return final

def arreglar_lista_fecha(lista):
    lista_arreglada = []
    for X in lista:
        valor = str(X)
        lista_arreglada.append(valor)
    return lista_arreglada

def agregar_al_archivo_de_texto(msj):
    with open('C:\\Users\\User\\OneDrive\\Escritorio\\Cosas UTN\\1er Cuatri\\Python\\Parcial\\resultado_batalla.txt', mode='a', encoding="utf-8") as archivo:
        archivo.write(msj)
    archivo.close()
