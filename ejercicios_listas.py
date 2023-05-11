from verificaciones import verificar_ingreso_y_texto

def lista_contador(lista:list, clave:str):
    '''
    se encarga de contar cada coincidencia que hay en la lista

    parametros:
    lista: lista en la cual se buscan las coincidencas
    clave: clave de diccionario que se quiere buscar
    '''
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
    '''
    se encarga de buscar la cantidad de tipos de algo existen en una lista

    parametros:
    lista: lista en la cual se buscan los tipos
    key: valor del diccionario a buscar los tipos

    retorno: un set con todos los tipos existentes
    '''
    lista_arreglada = []
    for personaje in lista:
        pj = personaje[key]
        pj = ajustar_str(pj)
        lista_arreglada.append(pj)
    tipos = set(lista_arreglada)
    return tipos

def ajustar_str(origen, reemplzado = "-", reemplazo = " "):
    '''
    se encarga de ajustar un string

    parametros:
    origen: string original
    reemplazado: valor a reemplazar
    reemplazo: valor con el cual reemplazar los datos

    retorno: string arreglado
    '''
    comparacion = origen.strip()
    comparacion = comparacion.replace(reemplzado, reemplazo)
    comparacion = comparacion.capitalize()
    return comparacion

def personajes_por_tipo(lista:list, clave:str):
    '''
    se encarga de imprimir los personajes que hay en cada tipo

    parametros:
    lista: lista en la cual buscar coincidencias
    clave: clave para buscar las coincidencas
    '''
    lista_filtrada = cantidad_tipos(lista, clave)
    for pj in lista_filtrada:
        print('\n')
        print(pj)
        for heroe in lista:
            comparado = ajustar_str(heroe[clave])
            if comparado == pj or (comparado.lower()).find(pj.lower()) != -1:
                print(f"Nombre: {heroe['nombre']}, Poder de Ataque {heroe['poder_ataque']}")

def personajes_por_habilidad(lista):
    '''
    se encarga de imprimir los personajes que hay en cada habilidad

    parametros:
    lista: lista en la cual se buscan las coincidencias
    '''
    habilidad = input("Ingresa una habilidad: ")
    habilidad = verificar_ingreso_y_texto(habilidad)
    for heroe in lista:
        if (heroe['habilidades'].lower()).find(habilidad.lower()) != -1:
            promedio = sacar_promedio(heroe['poder_pelea'], heroe['poder_ataque'])
            print(f"Nombre: {heroe['nombre']} | Promedio poder: {promedio}")

def sacar_promedio(X, Y):
    '''
    se encarga de sacar el promedio entre dos numeros

    parametros:
    X: primer valor
    Y: segundo valor

    retorno: Valor del promedio
    '''
    promedio = X + Y
    promedio = promedio/2
    return promedio
