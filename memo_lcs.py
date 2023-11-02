def lcs(n,m,x,y):
    if(x == 0 or y ==0):
        return 0 
    else:
        t=[[-1 for i in range(y+1)] for j in range(x+1)]
        if(n[x-1]==m[y-1]):
           t[x][y]=1 +lcs(n,m,x-1,y-1)
           return t[x][y]
        else:
            return max(lcs(n,m,x-1,y),lcs(n,m,x,y-1))
        

# following code is for the meomoization

if __name__ == '__main__':
    n = ['A', 'G', 'G', 'T', 'A', 'B']
    m = ['G', 'X', 'T', 'X', 'A', 'y','B']
    x = len(n)
    y = len(m)
     
    count = lcs(n, m, x, y)
    print(count)
