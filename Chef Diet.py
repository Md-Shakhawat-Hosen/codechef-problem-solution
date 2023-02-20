t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    li = list(map(int,input().split()))[:n]
    r = 0
    ind = 0
    c = False
    for i in range(n):
        s = li[i]+r
        if s >= k:
            s = abs(s-k)
            r = s
            c = True
        else:
            c = False
            ind = i
            break
    if c:
        print("YES")
    else:
        print("NO",ind+1)
