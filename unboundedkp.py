def knapsack(wt,v,W,n):
    t =[[0 for i in range(W+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if(i==0 or j==0):
                t[i][j]=0
            elif(wt[i-1]<=W):
                t[i][j]=max(v[i-1]+t[i][j-wt[i-1]],t[i-1][j])
            
            else:
                t[i][j]=t[i-1][j]
            
    return t[n][W]
                
                                
    
    
    
if __name__ == '__main__':
    v = [10, 30, 20]
    wt = [5, 10, 15]
    W = 100
    n = len(wt)
    print(knapsack(wt,v,W,n))