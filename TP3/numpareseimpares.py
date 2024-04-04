nums = []
numsImpares = []
numsPares = []
while len(nums) < 5:
    nums.append(int(input("Introduzca un numero: "))) 
    
for num in nums:
    if num % 2 == 0:
            numsPares.append(num)
    else:
        numsImpares.append(num)    

print("Los numeros pares son:", numsPares)
print("Los numeros impares son:", numsImpares)                 