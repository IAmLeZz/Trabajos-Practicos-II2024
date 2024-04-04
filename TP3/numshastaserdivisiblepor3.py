sum = 0

while True:
    num = int(input("Introduzca un número: "))
    while num != 0:
        sum += num % 10
        num = num // 10
        
    if sum % 3 == 0:
        print("La suma de los dígitos es divisible por 3")
        break;
    else:
        print("La suma de los dígitos no es divisible por 3")     
        sum = 0 
        


    

    

    