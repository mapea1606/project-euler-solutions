# Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def sumador_digitos(num):
    cadena = str(num)
    i = 0
    suma = 0
    while i < len(cadena):
        suma = suma + int(cadena[i])
        i += 1
    return suma


p = 2 ** 1000

print(p)
print(sumador_digitos(p))
