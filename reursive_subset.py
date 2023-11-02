def lcs_memo(str1:str, str2:str,x,y):
    if(x==0 or y==0):
        return 0 
    elif(str1[x-1]==str2[y-1]):
        return 1 + lcs_memo(str1, str2,x-1, y -1)
    else:
        return max(lcs_memo(str1, str2,x-1, y),lcs_memo(str1, str2,x, y -1))
if __name__ == '__main__':
   str1 = "AGGTAB"
   str2 = "GXTXAYB"
   x=str1.__len__()
   y=str2.__len__()
   z = lcs_memo(str1, str2,x, y)
   print(z)
    