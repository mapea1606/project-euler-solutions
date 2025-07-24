def es_primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

def suma_primos(num):
    i = 2
    s = 0
    while i <= num:
        if es_primo(i):
            p = i
            print(p)
            s = s + p
        i += 1
    return s

n = int(input("Introduce el numero: "))

print(suma_primos(n))
