t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int,input().split()))[:n]
    li1 = list(set(li))
    if len(li) == len(li1):
        print(n-1)
    elif len(li1) == 1:
        print(0)
    else:
        l = 0
        for i in range(len(li1)):
            c = li.count(li1[i])
            if c > l:
                l = c
        print(len(li)-l)