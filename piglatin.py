def getfirstchar(s):
    vowels = ['a','e','i','o','u']
    if(s[0] in vowels):
        return(0)
    elif(s[0] == 'q'):
        return(-1)
    else:
        return(1)

S = input().split()
#flag = getfirstchar(s)

for s in(S):
    flag = getfirstchar(s)
    if(flag == 0):
        print(s+'way',end = " ")
    elif(flag == -1):
        print(s[2:]+'quay',end = " ")
    else:
        print(s[1:]+s[0]+'ay',end = " ")