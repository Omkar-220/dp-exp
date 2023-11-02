def climb(n):
    if(n<=2):
        return n
    else:
        return climb(n-1)+(n-2)

def memo_climb(n):
    t = [None for i  in range(n+1) ]
    if(n<=2):
        return n
    if(t[n]!=None):
        return t[n]  
    t[n]= memo_climb(n-1)+memo_climb(n-2)
       
    return t[n]



def dp_climb(n):
   t = [None] * (n+1)
   t[0]= 0 
   t[1]=1 
   t[2]= 2
   
   for i in range(3,n+1):
        t[i] = t[i-1] + t[i-2]

        print(t[n]) 
        
   

    
    
if __name__ =='__main__':
    n =10 
    # print(memo_climb(n))
    # print(climb(n))
    print(dp_climb(n))
    
       

    