import math


def powerSet(arr):
    powers = []

    total = int(math.pow(2, len(arr)))

    for i in range(0, total):

        tempSet = []

        num = "{0:b}".format(i)

        while len(num) < len(arr):
            num = '0' + num

        for b in range(0, len(num)):
            if num[b] == '1':
                tempSet.append(arr[b])

        powers.append(tempSet)

    return powers


print(powerSet([1, 2, 3]))