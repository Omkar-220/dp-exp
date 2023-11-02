import sys 
def partitioning(string, i , j ):
    if(i>=j):
        return 0
    max = sys.maxsize
    for k in range(i,j):
        temp=(1+ partitioning(string,i,j)+partitioning(string, k+1, j ))
        max = min(temp,max)

    return max

        





if __name__ == '__main__':
    str1 = "ababbbabbababa"
    N = len(str1)
    if str1 == str1[::-1]:
        print(partitioning(str1, 0, N - 1))
    else:
        print(False)
    