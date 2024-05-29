# Contador de dígitos que devuelve el conteo
def counter(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

# Verificar si el numero es par o impar
def even_or_odd(num):
    if num % 2 == 0:
        return "El numero es par"
    else:
        return "El numero es impar"

# Convertir un numero decimal a binario
def decimal_to_binary(num):
    base = 0
    binary = 0
    while num > 0:
        binary += (num % 2) * (10**base)
        num //= 2
        base += 1
    return binary

def main():
    salir = False
    while salir == False:
        num_compuesto = 0
        for i in range(3):
            num = counter(int(input('Ingrese un numero: ')))
            num_compuesto = num_compuesto*10 + num

        print('El numero compuesto es:', num_compuesto)
        print(even_or_odd(num_compuesto))
        print('El binario del numero es: ', decimal_to_binary(num_compuesto))
        salir = input('Desea salir? (s/n): ') == 's'

main()


        