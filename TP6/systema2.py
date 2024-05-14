# Convertir segundos a hora, minuto, segundos
def convert_time(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_resto = (segundos % 3600) % 60
    return horas, minutos, segundos_resto

# Añadir el primer tiempo dado con el segundo
# Verificar si los segundos totales son mayores a 60 y sumarlos a los minutos
# Verificar si los minutos totales son mayores a 60 y sumarlos a las horas
def add_time1and2(horas2, minutos2, segundos2, segundos):
    horas1, minutos1, segundos1 = convert_time(segundos)
    segundos_total = segundos2 + segundos1
    minutos_total = minutos2 + minutos1
    horas_total = horas2 + horas1

    if segundos_total >= 60:
        minutos_total += segundos_total // 60
        segundos_total = segundos_total % 60

    if minutos_total >= 60:
        horas_total += minutos_total // 60
        minutos_total = minutos_total % 60

    return horas_total, minutos_total, segundos_total

def main():
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
                print(add_time1and2(horas2, minutos2, segundos2, segundos))
            else:
                print('Por favor, ingrese un valor entero mayor que 0 en la opción 1.')

main()