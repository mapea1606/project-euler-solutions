# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

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


