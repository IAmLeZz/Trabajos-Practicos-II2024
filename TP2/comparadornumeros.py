nums = []

while len(nums) < 3:
    nums.append(int(input("Introduzca un número: ")))

def numsAddComparison(nums):
    if nums[0] + nums[1] == nums[2]:
        return ("El tercer número es la suma del primero y segundo.")
    elif   nums[0] + nums[2] == nums[1]:
        return ("El segundo número es la suma del primero y tercero.")
    elif nums[1] + nums[2] == nums[0]:
        return ("El primer número es la suma del segundo y tercero.")          
    else :
        return ("No hay relación de suma entre los números.")    
print(numsAddComparison(nums))        