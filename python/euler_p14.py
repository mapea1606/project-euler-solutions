import time
def collatz(num):
    collatz_sequence = list()
    collatz_sequence.append(num)
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            collatz_sequence.append(num)
        else:
            num = 3*num + 1
            collatz_sequence.append(num)
    return collatz_sequence


n = 1000000
magnitudes = list()

while n >= 1:
    magnitudes.append([len(collatz(n)), n])
    n -= 1

magnitudes.sort()

print(magnitudes[len(magnitudes)-1])
print(time.process_time())
print(time.time())
