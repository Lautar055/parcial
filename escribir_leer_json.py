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
    titulo_archivo = titulo_archivo + ".json"
    conjunto = buscar_datos(valores[0], valores[1], lista)
    crear_json(conjunto, titulo_archivo)

def pedir_valores():
    union_valores = []
    valor_raza = input("Ingrese una raza: ")
    union_valores.append(valor_raza)
    valor_habilidad = input("Ingrese la habilidad: ")
    union_valores.append(valor_habilidad)
    return union_valores

def buscar_datos(primer_valor, segundo_valor, lista):
    lista_guardados = []
    for heroe in lista:
        lista_temporal = []
        if (heroe['raza'].lower()).find(primer_valor.lower()) != -1 and (heroe['habilidades'].lower()).find(segundo_valor.lower()) != -1:
            nombre = heroe['nombre']
            habilidades = heroe['habilidades'].lower()
            poder = heroe['poder_pelea']
        lista_temporal.append(nombre)
        habilidades = ajustar(habilidades, segundo_valor)
        lista_temporal.append(habilidades)
        lista_temporal.append(poder)
        final = join(lista_temporal, " - ")
        lista_guardados.append(final)
    return lista_guardados

def ajustar(valor, valor_eliminar):
    conjunto = valor.split("|$%")
    conjunto = conjunto.remove(valor_eliminar)
    conjunto.join(" + ")
    return conjunto

def leer_json():
    pass