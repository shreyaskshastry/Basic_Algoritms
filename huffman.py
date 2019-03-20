import heapq
from collections import defaultdict


def encode(frequency):
    heap = [[weights, [Char, '']] for Char, weights in frequency.items()]
    heapq.heapify(heap)
    while (len(heap) > 1):
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in (lo[1:]):
            pair[1] = '0' + pair[1]
        for pair in (hi[1:]):
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return (sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))


data = "Always aim on the stars at least u will end up on moon"
frequency = defaultdict(int)
for char in data:
    frequency[char] += 1

huff = encode(frequency)
print ("Characters".ljust(12) + "Frequency".ljust(10) + "HCode")
for p in huff:
    print (p[0].ljust(12) + str(frequency[p[0]]).ljust(10) + p[1])