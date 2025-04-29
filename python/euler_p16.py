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
