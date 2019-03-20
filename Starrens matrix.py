import numpy as np
counter = 0

def partitionMatrix(matrix):
    length = len(matrix)
    if(length % 2 is not 0):
        stack = []
        for x in range(length + 1):
            stack.append(float(0))
        length += 1
        matrix = np.insert(matrix, len(matrix), values=0, axis=1)
        matrix = np.vstack([matrix, stack])
    d = (length // 2)
    matrix = matrix.reshape(length, length)
    completedPartition = [matrix[:d, :d], matrix[d:, :d], matrix[:d, d:], matrix[d:, d:]]
    return completedPartition

def strassen(mA, mB):
    n1 = len(mA)
    n2 = len(mB)
    global an
    if(n1 and n2 <= an):
        return (mA * mB)
    else:
        print(mA)
        A = partitionMatrix(mA)
        B = partitionMatrix(mB)
        mc = np.matrix([0 for i in range(len(mA))]for j in range(len(mB)))
        C = partitionMatrix(mc)


        a11 = np.array(A[0])
        a12 = np.array(A[2])
        a21 = np.array(A[1])
        a22 = np.array(A[3])

        b11 = np.array(B[0])
        b12 = np.array(B[2])
        b21 = np.array(B[1])
        b22 = np.array(B[3])

        mone = np.array(strassen((a11 + a22), (b11 + b22)))
        mtwo = np.array(strassen((a21 + a22), b11))
        mthree = np.array(strassen(a11, (b12 - b22)))
        mfour = np.array(strassen(a22, (b21 - b11)))
        mfive = np.array(strassen((a11 + a12), b22))
        msix = np.array(strassen((a21 - a11), (b11 + b12)))
        mseven = np.array(strassen((a12 - a22), (b21 + b22)))

        C[0] = np.array((mone + mfour - mfive + mseven))
        C[2] = np.array((mthree + mfive))
        C[1] = np.array((mtwo + mfour))
        C[3] = np.array((mone - mtwo + mthree + msix))

        return np.array(C)

print("enter n for which we have 2^n elemnts in matrix")
an = int(input())
matrixA = []
matrixB = []
print("A:")
for i in range(an):
    lst = [int(x) for x in(input().split())]
    matrixA.append(lst)
#print(matrixA)
print("B:")
for i in range(an):
    lst = [int(x) for x in(input().split())]
    matrixB.append(lst)

#matrixB = [[1,2],[3,4]]
#matrixA = [[5,6],[7,8]]
matrixA = np.matrix(matrixA)
matrixB = np.matrix(matrixB)

matrixC = [[0 for i in range(len(matrixA))]for j in range(len(matrixA))]

print("C =")
print(strassen(matrixA, matrixB))