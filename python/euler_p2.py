f = list()
f.append(1)
f.append(2)
i = 2
s = 0
while f[i-2] < 4000000:
    f.append(f[i-1]+f[i-2])
#    print("f(",i-1,") =", f[i-2])
    if f[i-2]%2 == 0:
        print("f(",i-1,") =", f[i-2])
        s = s + f[i-2]

    i += 1

print("S =",s)
