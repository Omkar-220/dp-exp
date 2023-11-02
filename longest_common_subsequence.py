def substring(n,m,x,y):
    
       
        t = [[0 for i in range(y+1)] for j in range(x+1)]
        result = 0 
        # t= [[0 for i in range(x+1)]for j in range(y+1)]
        for i in range(x+1):
            for j in range(y+1): 
                if (i == 0 or j == 0):
                    t[i][j] = 0
                elif(n[i-1]==m[j-1]):
                    t[i][j] = t[i-1][j-1] + 1
                    result = max(result, t[i][j])
                else:
                    t[i][j] = 0 
        
        return result

n = 'abcddcba'
m = 'abcddcba'
 
x = len(n)
y = len(m)
 
print('Length of Longest Common Substring is',substring(n,m,x,y))
    
