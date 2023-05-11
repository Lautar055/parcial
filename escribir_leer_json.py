import json
from ejercicio_batalla import join

def crear_json(lista, nombre_archivo):
    with open(nombre_archivo, mode='w', encoding="utf-8") as archivo:
        for dato in lista:
            json.dump(dato, archivo)
    archivo.close()

def main_escribir_json(lista):
    valores = pedir_valores()
    titulo_archivo = join(valores, "_")
    titulo_archivo = titulo_archivo.replace(' ', '')
    titulo_archivo = titulo_archivo + ".json"
    conjunto = guardar_buscar_en_lista(lista, valores)
    crear_json(conjunto, titulo_archivo)
    return titulo_archivo

def pedir_valores():
    union_valores = []
    valor_raza = input("Ingrese una raza: ")
    union_valores.append(valor_raza)
    valor_habilidad = input("Ingrese la habilidad: ")
    union_valores.append(valor_habilidad)
    return union_valores

def guardar_buscar_en_lista(lista_original, lista_valores):
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
    conjunto = valor.split("|$%")
    if valor_eliminar in conjunto:
        conjunto.remove(valor_eliminar)
    if len(conjunto) > 1:
        conjunto.join(" + ")
    else:
        conjunto = conjunto[0]
    return conjunto

def leer_json(titulo):
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
    for heroe in lista:
        print(f"Nombre: {heroe['nombre']}")
        print(f"El poder de pelea es: {heroe['poder']} y las habilidades que tiene son: {heroe['habilidades']} sin contar la ingresada para la busqueda.")
