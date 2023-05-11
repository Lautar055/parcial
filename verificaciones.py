def verificar_ingreso_y_numero(valor_a_verificar):
    '''
    verifica la existencia y comprueva el valor, cambiandolo todas las veces que sea necesario

    parametros:
    valor_a_verificar: el valor que hay que verificar

    retorna el valor corregido
    '''

    while True:
        if not valor_a_verificar:
            valor_a_verificar = input("No se ingresó ningún valor. Ingrese un número: ")
        elif not valor_a_verificar.isnumeric():
            valor_a_verificar = input("El valor ingresado no es un número. Ingrese un número: ")
        else:
            break
    return valor_a_verificar

def verificar_ingreso_y_texto(valor_a_verificar):
    '''
    verifica la existencia y comprueva el valor, cambiandolo todas las veces que sea necesario

    parametros:
    valor_a_verificar: el valor que hay que verificar

    retorna el valor corregido
    '''

    while True:
        if not valor_a_verificar:
            valor_a_verificar = input("No se ingresó ningún valor. Ingrese un valor: ")
        elif valor_a_verificar.isnumeric():
            valor_a_verificar = input("El valor ingresado no es texto. Ingrese un valor: ")
        else:
            break
    return valor_a_verificar

def verificar_existencia(valor_a_verificar):
    '''
    verifica la existencia las veces que sea necesario

    parametros:
    valor_a_verificar: el valor que hay que verificar

    retorna el valor corregido
    '''

    while True:
        if not valor_a_verificar:
            valor_a_verificar = input("No se ingresó ningún valor. Ingrese un valor: ")
        else:
            break
    return valor_a_verificar
