allsubs = []
def GetSubsequences(arr, n) :
    size = int(math.pow(2, n) )
    for counter in range(1,size) :
        lst = []
        for j in range(0, n) :
            if (counter & (1<<j)) :
                lst.append(arr[j])
        allsubs.append(lst)
print(GetSubsequence([1,3,2,4,5],5))