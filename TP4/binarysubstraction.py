def binarySubstraction(a, b):
    # Calcula el complemento a uno de b
    b = ~b

    # Realiza la suma de a y el complemento a uno de b
    result = a + b + 1  # El '+1' es para tener en cuenta el acarreo en la suma binaria

    # Si el resultado es negativo, calcula su complemento a uno
    if result < 0:
        result = ~result

    return result
    
    
print(binarySubstraction(111, 111))
    