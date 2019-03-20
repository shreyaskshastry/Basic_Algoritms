import math


# runtime O(n log log n)
def sieve(limit):
    bools = []
    primes = []

    for i in range(1, limit):
        bools.append(True)

    for i in range(2, int(math.sqrt(limit)) + 1):
        if bools[i - 2]:
            for j in range(i * 2, limit + 1, i):
                bools[j - 2] = False

    for p in range(0, len(bools)):
        if (bools[p]):
            primes.append(p + 2)

    return primes


print
sieve(100)