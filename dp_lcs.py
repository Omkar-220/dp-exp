def lcs(n, m, x, y):
    # t=[[0 for i in range(y+1)]for j in range(x+1)]
    t = [[0 if i == 0 or j == 0 else -1 for i in range(y + 1)] for j in range(x + 1)]
    for i in range(x+1):
        for j in range(y+1):
            if(x==0 or y ==0):
                t[i][j]=0;
            elif(n[i-1]==m[j-1]):
                t[i][j] = 1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i][j-1], t[i-1][j])
                
    return t[x][y]

if __name__ == '__main__':
    n = ['A', 'B', 'C', 'D', 'E']
    m = ['F', 'G', 'H', 'I', 'J']
    x = len(n)
    y = len(m)
     
    count = lcs(n, m, x, y)
    print(count)
