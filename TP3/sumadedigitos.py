sum = 0
num = int(input("Introduzca un número: "))

while num != 0:
    sum += num % 10
    num = num // 10
print("La suma de los dígitos es:", sum)