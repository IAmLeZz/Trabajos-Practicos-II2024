num = int(input("Digite un número"))

if num == 1:
    print("No es perfecto")
elif num > 1:
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print("Es perfecto")
    else:
        print("No es perfecto")