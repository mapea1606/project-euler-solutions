# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def invertidor(cadena):
    reverso = ""
    i = len(cadena)
    while i > 0:
        reverso = reverso + cadena[i-1]
        i -= 1
    return reverso
        
def es_capicua(numero):
    str(numero)
    invertidor(numero)
    if numero == invertidor(numero):
        return True
    else:
        return False

i = 999
while i > 900:
    j = 999
    while j > 900:
        if es_capicua(str(i*j)):
            print(i,"x",j,"=",i*j)
        j -= 1
    i -= 1
