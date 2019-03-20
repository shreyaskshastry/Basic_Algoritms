from sympy import exp, I, pi, sympify
from math import log, ceil

def normal_form(d):
    return [sympify(d_i).expand(complex=True) for d_i in d]

def fft(n, a, depth=0):
    if n < len(a):
        raise ValueError("DFT index can't be smaller than array length")
    if log(n,2) != ceil(log(n,2)):
        raise ValueError("DFT index must be a power of 2")
    if len(a) == 1:
        d = []
        for i in range(n):
            d.append((a[0]))
    else:
        a0 = [a[i] for i in range(0, len(a), 2)]
        a1 = [a[i] for i in range(1, len(a), 2)]
        d0 = fft(int(n/2), a0, depth+1)
        d1 = fft(int(n/2), a1, depth+1)
        w_n = exp(I*2*pi/n)
        w = 1
        d = [0 for i in range(n)]
        for k in range(int(n/2)):
            x = w * d1[k]
            d[k] = d0[k] + x
            d[k+int(n/2)] = d0[k] - x
            w *= w_n
        d = normal_form(d)
    return d

def polymult(a, b):
    n = (len(a) + len(b) - 1) if b else (2 * len(a) - 1)
    n = 2**int(ceil(log(n,2)))                   # Round up to next power of 2.
    #Evaluation:
    d_a = fft(n, a)                                            # d_a = DFT_n(a)
    d_b = fft(n, b) if b else d_a                              # d_b = DFT_n(b)
    #Point-wise multiplication:
    d = []
    for i in range(n):
        d.append((d_a[i] * d_b[i]))                   # d = d_a * d_b
    d = normal_form(d)
    #print(d)
    #Interpolation:
    f = fft(n, d)                                       # f = DFT_n(d)

    r = []
    r.append(f[0]/n)
    for j in range(n-1,1,-1):
        r.append(f[j]/n)

    return r

if __name__=="__main__":
    print("coff of A(x):",end="")
    a = [int(x) for x in input().split()]
    print("coff of B(x):", end="")
    b = [int(x) for x in input().split()]
    #a = [1, 5]
    #b = [1, -3]
    print("C(x):",end="")
    print((polymult(a,b)))





