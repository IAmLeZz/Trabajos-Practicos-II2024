nums = []
numsQueTerminanCon3 = []
def numsThatEndIn3(nums):
   
    while len(nums) < 10:
        nums.append(int(input("Introduzca un número: ")))
    for num in nums:
        if num % 10 == 3:
            numsQueTerminanCon3.append(num)
    print("Hay", len(numsQueTerminanCon3), "números que terminan en 3: ", numsQueTerminanCon3)       

numsThatEndIn3(nums)                