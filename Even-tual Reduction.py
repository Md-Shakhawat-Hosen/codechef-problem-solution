t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    li = list(s)
    li.sort()
    flag = False
    if n % 2 == 0:
        for i in range(0, n - 1, 2):
            if li[i] != li[i + 1]:
                flag = True
                break
        if flag:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
