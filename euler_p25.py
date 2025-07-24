def rec_fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
def fibonacci(num):
    f = list()
    if num == 0:
        f.append(0)
        return f
    elif num == 1:
        f.append(0)
        f.append(1)
        return f
    elif num == 2:
        f.append(0)
        f.append(1)
        f.append(1)
        return f
    else:
        i = 3
        f.append(0)
        f.append(1)
        f.append(1)
        while i <= num:
            f.append(f[i-1]+f[i-2])
            i += 1
        return f

def indice_xdigitos(lista):
    i = 0
    while i < len(lista):
        if len(str(lista[i])) == 1000:
            return i
        i += 1

n = int(input("Enter the index: "))

print(fibonacci(n))
print(indice_xdigitos(fibonacci(n)))
