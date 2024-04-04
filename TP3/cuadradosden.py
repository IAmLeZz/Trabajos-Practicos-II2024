num = int(input("Digite un número"))

if len(str(num)) == 3:
    print("Número | Cuadrado")
    print("-----------------")
    for i in range(1, num + 1):
        print("{:<6} | {:<8}".format(i, i ** 2))
else:
    print("El número debe ser de 3 dígitos")      