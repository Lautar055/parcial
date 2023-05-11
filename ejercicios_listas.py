from verificaciones import verificar_ingreso_y_texto

def lista_contador(lista:list, clave:str):
    contador = 0
    lista_filtrada = cantidad_tipos(lista, clave)
    for pj in lista_filtrada:
        print(pj)
        for heroe in lista:
            comparado = ajustar_str(heroe[clave])
            if comparado == pj:
                contador += 1
        print(contador)
        contador = 0

def cantidad_tipos(lista, key):
    lista_arreglada = []
    for personaje in lista:
        pj = personaje[key]
        pj = ajustar_str(pj)
        lista_arreglada.append(pj)
    tipos = set(lista_arreglada)
    return tipos

def ajustar_str(origen, reemplzado = "-", reemplazo = " "):
    comparacion = origen.strip()
    comparacion = comparacion.replace(reemplzado, reemplazo)
    comparacion = comparacion.capitalize()
    return comparacion

def personajes_por_tipo(lista:list, clave:str):
    lista_filtrada = cantidad_tipos(lista, clave)
    for pj in lista_filtrada:
        print('\n')
        print(pj)
        for heroe in lista:
            comparado = ajustar_str(heroe[clave])
            if comparado == pj or (heroe['raza'].lower()).find(pj.lower()) != -1:
                print(f"Nombre: {heroe['nombre']}, Poder de Ataque {heroe['poder_ataque']}")

def personajes_por_habilidad(lista):
    habilidad = input("Ingresa una habilidad: ")
    habilidad = verificar_ingreso_y_texto(habilidad)
    for heroe in lista:
        if (heroe['habilidades'].lower()).find(habilidad.lower()) != -1:
            promedio = sacar_promedio(heroe['poder_pelea'], heroe['poder_ataque'])
            print(f"Nombre: {heroe['nombre']} | Promedio poder: {promedio}")

def sacar_promedio(X, Y):
    promedio = X + Y
    promedio = promedio/2
    return promedio
