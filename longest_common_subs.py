def lcs(n, m, x, y):
    if x == 0 or y == 0:
        return 0
    else:
        if n[x - 1] == m[y - 1]:
            return 1 + lcs(n, m, x - 1, y - 1)
        else:
            return max(lcs(n, m, x - 1, y), lcs(n, m, x, y - 1))


if __name__ == '__main__':
    n = ['B', 'C', 'A', 'A', 'C', 'D']
    m = ['A', 'C', 'D', 'B', 'A', 'C']
    x = len(n)
    y = len(m)
     
    count = lcs(n, m, x, y)
    print(count)
