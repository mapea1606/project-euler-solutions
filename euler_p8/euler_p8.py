def multiplicador(cadena):
    i = 0
    p = 1
    while i < len(cadena):
        p = p * int(cadena[i])
        i += 1
    return p

lectura = open("euler_p8.txt","r")
leer = lectura.read().strip()

i = 0
numero = ""
while i < len(leer):
    if leer[i] != "\n":
        numero = numero + leer[i]
    i += 1

productos = list()

i = 0
while i < 988:
    if multiplicador(numero[i:i+13]) != 0:
        productos.append(multiplicador(numero[i:i+13]))
    i += 1

productos.sort()
print(productos[len(productos)-1])

lectura.close()
