def counter(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

def evenorodd(num):
    if num % 2 == 0:
        return "el numero es par"
    else:
        return "el numero es impar"
    
def decimaltobinary(num):
    base = 0
    binary = 0
    while num > 0:
        binary += (num % 2) * (10**base)
        num //= 2
        base += 1
    return binary

num1 = int(input('ingrese un numero: '))
num2 = int(input('ingrese otro numero: '))
num3 = int(input('ingrese ultimo numero: '))

numCompuesto = counter(num1)*100+counter(num2)*10+counter(num3)

print('El numero compuesto es:', numCompuesto)


print(evenorodd(numCompuesto))
print('El binario del numero es: ', decimaltobinary(numCompuesto))


        