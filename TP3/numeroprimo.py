import math

num = int(input("Digite un número"))

if num == 1:
    print("No es primo")
elif num > 1:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print("No es primo")
            is_prime = False
            break
    if is_prime:
        print("Es primo")
