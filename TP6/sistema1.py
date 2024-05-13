def increasing_order(num1, num2, num3):
    firstNumber = 0
    secondNumber = 0
    thirdNumber = 0
    if num1 > num2 and num2 > num3:
        firstNumber = num1
        secondNumber = num2
        thirdNumber = num3
    elif num1 > num3 and num3 > num2:
        firstNumber = num1
        secondNumber = num3
        thirdNumber = num2
    elif num2 > num1 and num1 > num3:
        firstNumber = num2
        secondNumber = num1
        thirdNumber = num3
    elif num2 > num3 and num3 > num1:
        firstNumber = num2
        secondNumber = num3
        thirdNumber = num1
    elif num3 > num1 and num1 > num2:
        firstNumber = num3
        secondNumber = num1
        thirdNumber = num2
    else:
        firstNumber = num3
        secondNumber = num2
        thirdNumber = num1
    return firstNumber, secondNumber, thirdNumber

def conversion_from_meters_to_another_system(meters, system):
    if system == 1:
        return meters * 1.094
    if system == 2:
        return meters * 39.3701
    if system == 3:
        return meters * 100

def excede_a_x(num):
    n = 0
    suma = 0
    while suma <= num:
        n += 1
        suma += n
    return n
    
opcion = True        
print(':::MENU:::')
print('1. Orden creciente')
print('2. Conversión')
print('3. Excede a X')

while opcion:
    opcion = input('Ingrese una opción: ')
    if opcion == '1':
        num1 = int(input('Ingrese un número: '))
        num2 = int(input('Ingrese otro número: '))
        num3 = int(input('Ingrese un último número: '))
        print(increasing_order(num1, num2, num3))
    elif opcion == '2':
        meters = int(input('Ingrese una cantidad en metros: '))
        system = int(input('Ingrese el sistema al que desea convertir. 1 para yardas, 2 para pulgadas, 3 para centimetros): '))
        print(conversion_from_meters_to_another_system(meters, system))
    elif opcion == '3':
        num = int(input('Ingrese un número: '))
        print(excede_a_x(num))
