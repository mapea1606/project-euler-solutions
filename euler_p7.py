def es_primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

def primos(num):
    i = 2
    while i <= num:
        if es_primo(i):
            print(i)
        i += 1

def enesimo_primo(num):
    indice = 1
    i = 2
    while indice <= num:
        if es_primo(i):
#            print(i)
            primo = i
            indice += 1
        i += 1
    return primo

n = int(input("Introduce el índice del primo: "))

print(enesimo_primo(n))
