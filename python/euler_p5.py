def es_primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

def primos(num):
    i = 2
    primos = list()
    while i <= num:
        if es_primo(i):
            primos.append(i)
        i += 1
    print(primos)
    return primos

def completar_producto(lista, tope):
    i = 0
    p = 1
    while i < len(lista):
        q = 1
        while q < tope:
#            print(lista[i])
            q = q * lista[i] 
        q = q // lista[i]
        i += 1
        print(q)
        p = p * q 
    return p

def producto_primos(lista):
    i = 0
    p = 1
    while i < len(lista):
        p = p * lista[i]
        i += 1
    return p
    

n = int(input("Introduce el numero: "))

#print(producto_primos(primos(n)))
print(completar_producto(primos(n), n))
