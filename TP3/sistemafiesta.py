edades = []
generos = []

while edades.__contains__(0) == False: 
    edadIngresada = int(input("Digite la edad de la persona: "))
    
    if edadIngresada == 0:
        break;
    
    if edadIngresada >= 18:
        edades.append(edadIngresada)
        generos.append(input("Digite el género de la persona (F/M): "))
    else:
        print("La persona debe ser mayor de edad")    
print("Edades: ", edades)
print("Géneros: ", generos)
print("Hay %s mujeres" % generos.count("F") + " y %s hombres" % generos.count("M"))    