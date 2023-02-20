t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))[:2 * n]
    flag = False
    for i in range(len(li)):
        c = li.count(li[i])
        if c > 2:
            flag = True
            break

    if flag:
        print("NO")
    else:
        print("YES")