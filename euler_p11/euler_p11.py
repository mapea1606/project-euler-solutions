# Problem 11

lectura = open("euler_p11.txt","r")
leer = lectura.read().strip()

matriz = []
vector = []

i = 0
while i < len(leer):
    matriz = leer.split("\n")
    i += 1

for elem in matriz:
    vector = elem.split(" ")
    print(vector)


print(len(leer))
print(leer)

lectura.close()
