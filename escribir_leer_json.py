import json
from unidecode import unidecode
from ejercicio_batalla import join
from verificaciones import verificar_ingreso_y_texto

def crear_json(lista, nombre_archivo):
    '''
    se encarga de crear un archivo en formato json

    parametros:
    lista: lista que recive con los datos para pasar al archivo
    nombre_archivo: Nombre con el cual se crea el archivo
    '''
    with open(nombre_archivo, mode='w', encoding="utf-8") as archivo:
        for dato in lista:
            json.dump(dato, archivo)
            archivo.write(",\n")
    archivo.close()

def main_escribir_json(lista):
    '''
    se encarga de la funcionalidad principal y ejecucion de la mayoria de funciones 
        del archivo referentes a la creacion del archivo json

    parametros:
    lista: lista necesaria para el correcto funcionamiento de la mayoria de funciones

    retorno: titulo del archivo json creado
    '''
    valores = pedir_valores()
    titulo_archivo = join(valores, "_")
    titulo_archivo = titulo_archivo.replace(' ', '')
    titulo_archivo = titulo_archivo + ".json"
    conjunto = guardar_buscar_en_lista(lista, valores)
    crear_json(conjunto, titulo_archivo)
    return titulo_archivo

def pedir_valores():
    '''
    se encarga de pedir valores y de unirlos en una lista

    retorno: retorna la lista con los valores que pide
    '''
    union_valores = []
    valor_raza = input("Ingrese una raza: ")
    valor_raza = verificar_ingreso_y_texto(valor_raza)
    union_valores.append(valor_raza)
    valor_habilidad = input("Ingrese la habilidad: ")
    valor_habilidad = verificar_ingreso_y_texto(valor_habilidad)
    union_valores.append(valor_habilidad)
    return union_valores

def guardar_buscar_en_lista(lista_original, lista_valores):
    '''
    se encarga de guardar el nombre, el poder de ataque y las habilidades de los personajes que cumplan con los 2 parametros

    parametros:
    lista_original: lista de diccionarios en la cual estan los datos
    lista_valores: lista con los parametros para hacer la busqueda

    retorno: una lista con los datos arreglados (Siendo una lista, por el caso de que halla más de una coincidencia)
    '''
    lista_retorno = []
    for heroe in lista_original:
        if heroe['raza'].lower() == lista_valores[0].lower() and heroe['habilidades'].find(lista_valores[1]) != -1:
            nombre = heroe['nombre']
            habilidades = heroe['habilidades']
            txt_habilidad = ajustar(habilidades, lista_valores[1])
            poder = heroe['poder_ataque']
            str_poder = str(poder)
            lista_temporal = [nombre, str_poder, txt_habilidad]
            final = " - ".join(lista_temporal)
            lista_retorno.append(final)
    return lista_retorno

def ajustar(valor, valor_eliminar):
    '''
    se encarga de ajustar un string y de eliminar una parte en caso de haberlo

    parametros:
    valor: valor completo a arreglar
    valor_eliminar: valor a eliminar

    retorno: retorna el string arreglado
    '''
    valor = unidecode(valor)
    conjunto = valor.split("|$%")
    if valor_eliminar in conjunto:
        conjunto.remove(valor_eliminar)
    if len(conjunto) > 1:
        conjunto = " + ".join(str(elemento) for elemento in conjunto)
    else:
        conjunto = conjunto[0]
    return conjunto

def leer_json(titulo):
    '''
    se encarga de la lectura de un archivo json creado previamente

    parametro:
    titulo: titulo del archivo a leer
    '''
    separador = " - "
    with open(titulo, mode='r', encoding="utf-8") as archivo:
        dvz_lista = []
        for linea in archivo:
            linea = linea.rstrip("\n")
            columna = linea.split(separador)
            nombre = columna[0]
            poder = columna[1]
            habilidades = columna[2]
            dvz_lista.append({
                'nombre' : nombre,
                'poder' : poder,
                'habilidades' : habilidades
            })
        imprimir_cada_elemento_lista(dvz_lista)

def imprimir_cada_elemento_lista(lista):
    '''
    se encarga de imprimir por partes una lista de diccionarios

    parametros:
    lista: lista de diccionarios a imprimir
    '''
    for heroe in lista:
        print(f"Nombre: {heroe['nombre']}")
        print(f"El poder de pelea es: {heroe['poder']} y las habilidades que tiene son: {heroe['habilidades']} sin contar la ingresada para la busqueda.")
