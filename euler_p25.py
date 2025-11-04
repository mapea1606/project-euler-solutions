# Problem 25

# The Fibonacci sequence is defined by the recurrence relation:
# F_n = F_{n - 1} + F_{n - 2}, where F_1 = 1 and F_2 = 1.
# Hence the first 12 terms will be:
# F_1 = 1
# F_2 = 1
# F_3 = 2
# F_4 = 3
# F_5 = 5
# F_6 = 8
# F_7 = 13
# F_8 = 21
# F_9 = 34
# F_10 = 55
# F_11 = 89
# F_12 = 144
# The 12th term, F_12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

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
