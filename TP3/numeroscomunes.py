num1= int(input("Digite un número: "))
num2= int(input("Digite un número: "))

digitosComunes = []

for i in str(num1):
    for j in str(num2):
        if i == j:
            digitosComunes.append(i)   

print("Los dígitos comunes son: ", digitosComunes)            