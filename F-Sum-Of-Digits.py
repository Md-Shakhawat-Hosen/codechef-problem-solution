n = int(input())
for x in range(n):
    inp = int(input())
    sum = 0
    while inp != 0:
        mod = int(inp % 10)
        sum = sum + mod
        inp = int(inp / 10)

    print(sum)

