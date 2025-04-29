s = 0
i = 1
while i <= 1000:
    s = s + i**i
    i += 1

cadena = str(s)
print(cadena[len(cadena)-10:len(cadena)])

