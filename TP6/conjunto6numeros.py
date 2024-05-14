def palindrome(n):
    rev = 0
    temp = n
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10
    return n == rev

def main():
    suma = 0
    count = 0
    capicuas = 0
    for i in range(6):
        num = int(input('Ingrese el número: '))
        if num % 7 == 0:
            suma += num
            count += 1
        if palindrome(num):
            capicuas += 1
            print(f"El número {num} es capicúa.")

    if count > 0:
        promedio = suma / count
        print("El promedio de los números múltiplos de 7 es: ", promedio)
    else:
        print("No se ingresaron números múltiplos de 7.")

    print('Se ingresaron ',capicuas, 'números capicúas.')
    
main()


    