# Problem 11

lectura = open("euler_p11.txt","r")
leer = lectura.read().strip()

matriz = []

i = 0
while i < len(leer):
    matriz = leer.split("\n")
    i += 1

for i in range(len(matriz)):
    matriz[i] = matriz[i].split(" ")

for vector in matriz:
    for i in range(len(vector)):
        vector[i] = int(vector[i])

for elem in matriz:
    print(elem)

cuartetas = []
vector = matriz[0]
i = 0
while i <= len(vector) - 4:
    cuartetas.append(vector[i:i+4])
    #print(vector[i:i+4])
    i += 1

for elem in cuartetas:
    print(elem)

lectura.close()
