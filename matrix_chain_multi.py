import sys
def mcm(p,i , j ):
    if( i>= j ):
        return 0
    
    min = sys.maxsize
    
    for k in range(i , j):
        temp = (mcm(p , i , k)
        +mcm(p,k+1,j)
        +p[i-1]*p[k]*p[j])
        
        if(temp < min):
            min = temp
    return min
    

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3]
    N = len(arr)
    print(mcm(arr , 1,N-1 ))
