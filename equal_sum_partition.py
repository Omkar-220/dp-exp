def partition(arr,sum,n):
    if(sum%2!=0):
        return False
    else:
        t = ([[False for  i in range(sum+1)] for i in range(n+1)])
        for i in range(n+1):
            t[i][0]=True
        for i in range(1,sum+1):
            t[0][i]=False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if j < arr[i-1]:
                t[i][j]=t[i-1][j]
            if(j>=arr[i-1]):
                t[i][j]=t[i-1][j]or t[i-1][j-arr[i-1]]
    
    
    return t[n][sum]
        
       
if __name__ == '__main__':
    arr = [1,1,1,1]
    n = len(arr)
    sum = sum(arr)//2
    res = partition(arr,sum,n)
    print(res)
    
    
    
