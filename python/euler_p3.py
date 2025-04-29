def es_primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

n = int(input("Ingresa el numero: "))
i = 2

print("Es primo?: ", es_primo(n))

while i <= n:
    if es_primo(i):
        multiplicidad = 0
        while n % i == 0:
            aux = n / i
            n = aux
            multiplicidad += 1
        if multiplicidad != 0:
            print("Primo:", i, "Multiplicidad:", multiplicidad)
    i += 1
