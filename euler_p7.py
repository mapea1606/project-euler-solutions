# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001 st prime number?

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
