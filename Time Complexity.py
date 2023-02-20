n = int(input())
for x in range(n):
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    if a == b:
        print("NO")
    elif a > b:
        print("YES")
    else:
        print("NO")