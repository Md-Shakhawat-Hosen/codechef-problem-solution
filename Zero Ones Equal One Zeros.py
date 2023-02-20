# t = int(input())
# for i in range(t):
#     n = int(input())
#     if n % 2 == 0:
#         for i in range(n//2):
#             print(1,end="")
#             print(0,end="")
#         print()
#     if n % 2 == 1:
#         for i in range((n-1)//2):
#             print(0,end="")
#             print(1,end="")
#         print(0,end="")
#         print()
def findResult(li,n):
    c = 0
    for i in range(0, n - 1, 2):
        if li[i] != li[i + 1]:
            c = li[i]
            break
        else:
            continue
    return c



t = int(input())
for i in range(t):
    n = int(input())
    li = []
    for i in range(n):
        li.append(int(input()))

    li.sort()
    c = 0
    if n % 2 == 0:
        c = findResult(li,len(li))
        print(c)
    else:
        c = findResult(li,len(li))
        e = li.count(li[-1])
        if e % 2 == 1:
            print(li[-1])
        else:
            print(c)


