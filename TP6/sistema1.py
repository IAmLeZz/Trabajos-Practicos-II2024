# Ordenar los números dados de manera ascendiente
def increasing_order(num1, num2, num3):
    first_number = 0
    second_number = 0
    third_number = 0
    
    if num1 > num2:
        if num1 > num3:
            first_number = num1
            if num2 > num3:
                second_number = num2
                third_number = num3
            else:
                second_number = num3
                third_number = num2
        else:
            first_number = num3
            second_number = num1
            third_number = num2
    else:
        if num2 > num3:
            first_number = num2
            if num1 > num3:
                second_number = num1
                third_number = num3
            else:
                second_number = num3
                third_number = num1
        else:
            first_number = num3
            second_number = num2
            third_number = num1
    
    return first_number, second_number, third_number

# Convertir metros a otro sistema
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


def main():    
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

main()
