n = int(input())
for x in range(n):
    inp = input().split()
    value1 = int(inp[0])
    value2 = int(inp[1])
    make_burger = min(value1,value2)
    print(make_burger)