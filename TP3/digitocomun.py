num1 = int(input("Escriba un número de un digito: "))

if num1 < 0 or num1 > 9:
    print("El número no es de un dígito.")
    exit()
else:
    num2 = int(input("Escriba un número de cualquier cantidad de dígitos."))

    found = False
    for i in str(num2):
        if i == str(num1):
            found = True
            break

    if found:
        print("Verdadero")
    else:
        print("Falso")