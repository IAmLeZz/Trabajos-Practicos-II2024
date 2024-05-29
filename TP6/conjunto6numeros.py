# Para verificar si un número es capicúa, se inicia una variable rev en 0 y se guarda el número en una variable temporal. 
# Luego, se itera mientras la variable temporal sea distinta de 0. 
# En cada iteración, se multiplica rev por 10 y se le suma el 10% de la variable temporal (último dígito). 
# Luego, se divide la variable temporal entre 10. 
# Finalmente, se retorna si el número es igual a rev.
def palindrome(n):
    rev = 0
    temp = n
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10
    return n == rev

def main():
    salir = False
    while salir == False:
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
                print('El número',num ,'es capicúa.')

        if count > 0:
            promedio = suma / count
            print("El promedio de los números múltiplos de 7 es: ", promedio)
        else:
            print("No se ingresaron números múltiplos de 7.")

        print('Se ingresaron ',capicuas, 'números capicúas.')
        salir = input('Desea salir? (s/n): ') == 's'
    
main()


    