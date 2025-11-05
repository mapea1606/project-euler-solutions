# Problem 48

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

s = 0
i = 1
while i <= 1000:
    s = s + i**i
    i += 1

cadena = str(s)
print(cadena[len(cadena)-10:len(cadena)])

