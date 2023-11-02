def coin_change(coins , target , n):
    t = [[0 for i in range(target+1)] for i in range(n+1)]
    for i in range(n+1):
        t[i][0]= 1 
    for i in range(1 , n+1):
        for j in range(1 ,target+1):
            if(coins[i-1]<= target):
                t[i][j]= t[i-1][j] +t[i][j-coins[i-1]]
            else:
                t[i][j]= t[i-1][j]
                
    else:
        return t[n][target]





    
coins = [1, 2, 5]
target = 12
n =len(coins)
num_ways = coin_change(coins, target,n)
print(num_ways)