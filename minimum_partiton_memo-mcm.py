import sys 
def palindrome(X):
    return X == X[::-1]
def partition(string , i , j, t ):
    if(i>=j or palindrome(string[i:j+1])):
        t[i][j]= 0 
        return 0 
    if(t[i][j]!= -1):
        return t[i][j]
    
    minin = float('inf')
    for k in range(i,j):
        if t[i][k] != -1:
            left = t[i][k]
        else:
            left = partition(string,i,k,t)
            t[i][j]=left
        if(t[k+1][j]!= -1):
            right = t[i][k]
        else:
            partition(string, k+1 , j , t)
            right = t[k+1][j]
        
        temp = left+1
        # temp= (1+partition(string, i , k,t)
        #        +partition(string, k+1 , j,t ))
        # 1 + partition(string, i, k, t) + partition(string, k + 1, j, t))
        
        minin = min (temp,minin)
        
        t[i][j] = minin
        
    return minin
        

    
def main():
    string = "ababbbabbababa"
    N = len(string)
    t = [[-1 for i in range(N)] for j in range(N)]
    print("Min cuts needed for Palindrome Partitioning is ", partition(string, 0, N - 1, t))

if __name__ == '__main__':
    main()