def decimaltobinary(n):
    if n < 0:
        return 'Los números negativos no están permitidos'
    if n == 0:
        return '0'
    if n > 0:
        binary = ''
        while n > 0:
            binary = n % 2, binary
            n = n // 2
        return binary

print(decimaltobinary(12))