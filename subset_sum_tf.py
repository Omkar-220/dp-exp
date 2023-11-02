def summ(wt,sum,n):
    t = ([[False for  i in range(sum+1)] for i in range(n+1)])
    for i in range(n+1):
        t[i][0]=True
    for i in range(1,sum+1):
        t[0][i]=False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j < wt[i-1]:
                t[i][j]=t[i-1][j]
            if(j>=wt[i-1]):
                t[i][j]=t[i-1][j]or t[i-1][j-wt[i-1]]
    
    print(t[n][sum])
            



if __name__=='__main__':
    wt = [3, 34, 4, 12, 5, 2]
    sum = 34
    n = len(wt)
    summ(wt,sum,n)
    
    
