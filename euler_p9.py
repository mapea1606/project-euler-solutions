import math

i = 1
while i < 500:
    j = 1
    while j < 500:
        if i + j + math.sqrt(i*i+j*j) == 1000:
            p = i*j*math.sqrt(i*i+j*j)
            break
        j += 1
    i += 1

print(p)


