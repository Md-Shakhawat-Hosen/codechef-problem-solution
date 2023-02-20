T = int(input())
for x in range(T):
    size_array = int(input())
    a = input().strip().split()[:size_array]
    lis = list(map(int, a))
    a = min(lis)
    c = 0
    for i in lis:
        if i % a != 0:
            c = 1
            break
    if c == 1:
        print(size_array)
    else:
        print(size_array - lis.count(a))













