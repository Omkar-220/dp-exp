import sys
t =[[-1 for i in range(100)] for j in range(100)]
def mcm(p , i , j ):
    if(i>=j):
        return 0
    if(t[i][j]!=-1):
        return t[i][j]
    t[i][j] = sys.maxsize
    for k in range(i,j):
        t[i][j] = min(t[i][j],mcm(p , i , k)
        +mcm(p,k+1,j)
        +p[i-1]*p[k]*p[j])
        
    return t[i][j]
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3]
    N = len(arr)
    print(mcm(arr,0, N-1))
