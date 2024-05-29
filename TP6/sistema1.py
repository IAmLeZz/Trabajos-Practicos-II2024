# Ordenar los números dados de manera creciente
def increasing_order(num1, num2, num3):
    # Inicializar las variables
    max_num = mid_num = min_num = None

    # Encontrar el número máximo
    if num1 >= num2 and num1 >= num3:
        max_num = num1
        # Determinar el número medio y el número mínimo
        if num2 >= num3:
            mid_num = num2
            min_num = num3
        else:
            mid_num = num3
            min_num = num2
    elif num2 >= num1 and num2 >= num3:
        max_num = num2
        # Determinar el número medio y el número mínimo
        if num1 >= num3:
            mid_num = num1
            min_num = num3
        else:
            mid_num = num3
            min_num = num1
    else:
        max_num = num3
        # Determinar el número medio y el número mínimo
        if num1 >= num2:
            mid_num = num1
            min_num = num2
        else:
            mid_num = num2
            min_num = num1

    return max_num, mid_num, min_num

# Convertir metros a otro sistema
def conversion_from_meters_to_another_system(meters, system):
    inch = 0.0254
    feet = inch * 12
    yard = feet * 3
    
    if system == 1:
        return 'yardas: ', meters / yard
    if system == 2:
        return 'pulgadas: ', meters / inch
    if system == 3:
        return 'centimetros: ', meters / 0.01
    
# Inicializar n (número actual que será sumado) y suma
# Mientras la suma sea menor o igual al número ingresado se sumará n a la suma y se incrementará n en 1
# Devolver n
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
