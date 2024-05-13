n = int(input('ingrese un numero de al menos 2 digitos: '))
d = int(input('ingrese el valor de d (un digito): '))
x = int(input('ingrese el valor de x (un digito): '))

def reemplazar_version_string(n, d, x):
    n = str(n)
    x = str(x)
    d = str(d)
    n = n.replace(d, x)
    return n

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

print(reemplazar_version_int(n, d, x))

