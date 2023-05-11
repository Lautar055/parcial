def verificar_ingreso_y_numero(valor_a_verificar):
    while True:
        if not valor_a_verificar:
            valor_a_verificar = input("No se ingresó ningún valor. Ingrese un número: ")
        elif not valor_a_verificar.isnumeric():
            valor_a_verificar = input("El valor ingresado no es un número. Ingrese un número: ")
        else:
            break
    return valor_a_verificar

def verificar_ingreso_y_texto():
    while True:
        if not valor_a_verificar:
            valor_a_verificar = input("No se ingresó ningún valor. Ingrese un valor: ")
        elif valor_a_verificar.isnumeric():
            valor_a_verificar = input("El valor ingresado no es texto. Ingrese un valor: ")
        else:
            break
    return valor_a_verificar

def verificar_existencia():
    while True:
        if not valor_a_verificar:
            valor_a_verificar = input("No se ingresó ningún valor. Ingrese un valor: ")
        else:
            break
    return valor_a_verificar
