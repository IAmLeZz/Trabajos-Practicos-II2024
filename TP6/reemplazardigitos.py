# Es lo mismo que lo de abajo, pero haciendo conversión de datos. 
def reemplazar_version_string(n, d, x):
    n = str(n)
    x = str(x)
    d = str(d)
    n = n.replace(d, x)
    return n

# Reemplazar digitos d que están en n, por x. Descomponer el número y hacer las verificaciones necesarias. 
def reemplazar_version_int(n, d, x):
    result = 0
    temp = 1
    while n > 0:
        digit = n % 10
        if digit == d:
            digit = x
        result += digit * temp
        temp *= 10
        n //= 10
    return result

def main():
    n = int(input('Ingrese un numero de al menos 2 digitos: '))
    d = int(input('Ingrese el valor de d (un digito): '))
    x = int(input('Ingrese el valor de x (un digito): '))
    print(reemplazar_version_int(n, d, x))

