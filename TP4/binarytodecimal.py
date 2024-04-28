def binaryToDecimal(binary):
   decimal = 0
   for digit in binary:
       decimal = decimal*2 + int(digit)
   return decimal

print(binaryToDecimal('1100'))