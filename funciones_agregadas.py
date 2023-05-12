from unidecode import unidecode

def guardar_saiyan(lista):
    lista_saiyan = []
    for heroe in lista:
        if heroe['raza'].find('Saiyan') != -1:
            lista_saiyan.append(heroe)
    return lista_saiyan

def aumento(lista):
    lista_retorno = []
    for heroe in lista:
        id_pj = heroe['id']
        nombre = heroe['nombre']
        raza = heroe['raza']
        poder_pelea = heroe['poder_pelea']
        poder_ataque = heroe['poder_ataque']
        habilidades = heroe['habilidades']

        poder_pelea = aumento_segun_porcentaje(poder_pelea, 50)
        poder_ataque = aumento_segun_porcentaje(poder_ataque, 70)
        habilidades = habilidades + "|$%transformación nivel dios"
        habilidades = unidecode(habilidades)

        lista_retorno.append({
            "id" : int(id_pj),
            "nombre" : nombre,
            "raza" : raza,
            "poder_pelea" : int(poder_pelea),
            "poder_ataque" : int(poder_ataque),
            "habilidades" : habilidades,
        })
    return lista_retorno

def aumento_segun_porcentaje(numero:int, porcentaje:int):
    numero_calculado = numero + (porcentaje * numero / 100)
    return numero_calculado

def join_lista_para_csv(lista):
    lista_strings_pj = []
    for heroe in lista:
        texto = (f"{heroe['id']},{heroe['nombre']},{heroe['raza']},{heroe['poder_pelea']},{heroe['poder_ataque']},{heroe['habilidades']}\n")
        lista_strings_pj.append(texto)
    return lista_strings_pj

def guardar_en_csv(nombre_archivo, lista):
    with open(nombre_archivo, mode='w', encoding="utf-8") as archivo:
        for elemento in lista:
            archivo.write(elemento)

def main_aumento(lista):
    lista_saiyan = guardar_saiyan(lista)
    lista_saiyan_aumentada = aumento(lista_saiyan)
    lista_texto_saiyan = join_lista_para_csv(lista_saiyan_aumentada)
    guardar_en_csv("Saiyan_arreglos.csv", lista_texto_saiyan)
