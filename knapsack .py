def knapsack(weight,profit,w,n):
    t =[[0 for x in range(w+1)] for x in range (n+1)]
    for i in range (n+1):
        for j in range(w+1):
            if i==0 or w==0 :
                t[i][j]=0
            elif weight[i-1]<=W:
                t[i][j]=max(profit[i-1]+t[i-1][w-weight[i-1]],
                            t[i-1][j])
            else:
                t[i][j]=t[i-1][W]
    
    return t[n][W]

                
        
            
if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(knapsack(weight,profit,W,n))