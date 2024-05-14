def decimal_to_binary(n):
    temp = 0
    binary = 0
    if n > 0:
       while n > 0:
           binary = binary + (n % 2) * (10 ** temp)
           n = n // 2
           temp += 1
    return binary
     
print(decimal_to_binary(50))