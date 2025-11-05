# Problem 13

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# You can see the number in the euler_p13.txt file.

lectura = open("euler_p13.txt","r")

# leer = lectura.read().strip()
# i = 0
# numero = ""
# while i < len(leer):
#     if leer[i] != "\n":
#         numero = numero + leer[i]
#     i += 1
# 
# print(numero)
# print(len(numero))
# 
# i = 0
# s = 0
# while i < len(numero):
#     s = s + int(numero[i])
#     i += 1
# 
# print(s)

numeros = list()

i = 0
while i < 100:
    numeros.append(lectura.readline().rstrip())
    i += 1

print(numeros)
print(len(numeros))

i = 0
s = 0
while i < 100:
    s = s + int(numeros[i])
    i += 1

print(s)
suma = str(s)
print(suma[0:10])

lectura.close()
