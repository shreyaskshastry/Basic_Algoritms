def longest_palindrome(text):
    N = len(text)
    if(N == 0 or N == 1):
        return (text)
    N = 2 * N + 1
    L = [0] * N
    L[0], L[1] = 0, 1
    C, R, i = 1, 2, 0
    iMirror, maxLPSLength, maxLPSCenterPosition = 0, 0, 0
    start,end,diff = -1,-1,-1

    for i in range(2, N):
        iMirror = 2 * C - i
        L[i] = 0
        diff = R - i

        if(diff > 0):
            L[i] = min(L[iMirror], diff)

        try:
            while ((i + L[i]) < N and (i - L[i]) > 0) and (((i + L[i] + 1) % 2 == 0) or (text[int((i + L[i] + 1) / 2)] == text[int((i - L[i] - 1) / 2)])):
                L[i] += 1
        except Exception as e:
            pass

        if(L[i] > maxLPSLength):
            maxLPSLength = L[i]
            maxLPSCenterPosition = i

        if(i + L[i] > R):
            C = i
            R = i + L[i]

    start = int((maxLPSCenterPosition - maxLPSLength) / 2)
    end = start + maxLPSLength - 1
    return(text[start:end + 1])