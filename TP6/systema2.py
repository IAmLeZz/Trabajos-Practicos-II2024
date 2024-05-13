def convert_time(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundosResto = (segundos % 3600) % 60
    return horas, minutos, segundosResto

def add_time1and2(horas2, minutos2, segundos2):
    horas1, minutos1, segundos1 = convert_time(segundos)
    
    segundosTotal = segundos2 + segundos1
    minutosTotal = minutos2 + minutos1
    horasTotal = horas2 + horas1

    if segundosTotal >= 60:
        minutosTotal += segundosTotal // 60
        segundosTotal = segundosTotal % 60

    if minutosTotal >= 60:
        horasTotal += minutosTotal // 60
        minutosTotal = minutosTotal % 60

    return horasTotal, minutosTotal, segundosTotal

opcion = True 
print(':::MENU:::')
print('1. Ingresar Valor')
print('2. Horas / Minutos / Segundos')
print('3. Sumar tiempo')

while opcion:
    opcion = input('Ingrese una opción: ')
    if opcion == '1':
        segundos = int(input('Ingrese un valor entero mayor que 0: '))
        if segundos <= 0:
            print('Por favor, ingrese un valor mayor que 0.')
        else:
            print('Actualmente está utilizando:', segundos, 'segundos. ¿Desea cambiar la cantidad de segundos? Y/N')
            respuesta = input()
            if respuesta == 'Y':    
                segundos = int(input('Ingrese un valor entero mayor que 0: '))
            else:
                segundos = segundos
    elif opcion == '2':
        if segundos != 0:
            print(convert_time(segundos))
        else:
            print('Por favor, ingrese un valor entero mayor que 0 en la opción 1.')
    elif opcion == '3':
        if segundos != 0:
            horas2 = int(input('Ingrese las horas: '))
            minutos2 = int(input('Ingrese los minutos: '))
            segundos2 = int(input('Ingrese los segundos: '))
            print(add_time1and2(horas2, minutos2, segundos2))
        else:
            print('Por favor, ingrese un valor entero mayor que 0 en la opción 1.')