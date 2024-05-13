def decimaltobinary(n):
    temp = 0
    binary = 0
    if n > 0:
       while n > 0:
           binary = binary + (n % 2) * (10 ** temp)
           n = n // 2
           temp += 1
    return binary
     
print(decimaltobinary(50))