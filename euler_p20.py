def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def sumador_digitos(num):
    cadena = str(num)
    i = 0
    suma = 0
    while i < len(cadena):
        suma = suma + int(cadena[i])
        i += 1
    return suma

n = int(input("Enter the number: "))

print(factorial(n))
print(sumador_digitos(factorial(n)))
