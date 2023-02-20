t = int(input())
for i in range(t):
    n,b = map(int,input().split())
    li = []
    for i in range(n):
        w,h,p = map(int,input().split())
        if b >= p:
            li.append(w*h)

    if len(li) == 0:
        print("no tablet")
    else:
        print(max(li))
