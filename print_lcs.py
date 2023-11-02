def lcs_pr(a,b, x, y):
    t= [[0 for i in range(y+1)]for i in range (x+1)]
    for i in range(x+1):
        for j in range(y+1):
            
            if(x==0 or j ==0 ):
                t[i][j]= 0
            elif(a[i-1]==b[j-1]):
                t[i][j]= t[i-1][j-1]+1
            else:
                t[i][j]= max(t[i-1][j],t[i][j-1])
             
    i = x
    j = y
    lcs=""
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs += a[i - 1]# append the element 
            i -= 1
            j -= 1
        elif t[i - 1][j] > t[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs = lcs[::-1]
    return lcs
    
            


a = "abcddcba"
b = "xyzza"
x= len(a)
y=len(b)
print(lcs_pr(a, b,x,y))


# n = 'abcddcba'
# m = 'abcddcba'/