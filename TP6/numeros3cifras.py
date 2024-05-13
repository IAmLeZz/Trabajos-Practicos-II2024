def getnumbers(n):
    c1 = n // 100
    c2 = (n // 10) % 10
    c3 = n % 10

    print(c1, c2, '-', c1, c3, '-', c2, c1, '-', c2, c3, '-', c3, c1, '-', c3, c2)

while True:
    n = int(input('Introduce un número de 3 cifras (o 0 para salir): '))
    if n == 0:
        break
    elif n < 100 or n > 999:
        print('Por favor, introduce un número de 3 cifras.')
    else:
        getnumbers(n)
