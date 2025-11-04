# Problem 20
# n! means n (n - 1) ... 3 2 1.
# For example, 10! = 10 9 ... 3 2 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!.

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
