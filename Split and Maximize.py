# T = int(input())
# for x in range(T):
#     size = int(input())
#     inp = input().split()[:size]
#     li = list(map(int,inp))
#     max_value = max(li)
#     li.remove(max_value)
#     for i in range(max_value):
#         li.append(1)
#     result = len(li) - 1
#     print(result*len(li))


# cook your dish here

n = int(input())
for x in range(n):
    inp = input().split()
    a = int(inp[0])
    b = int(inp[1])
    sum = a + b
    count = 0
    for x in range(2,sum+1):
        if sum % x == 0:
            count = count + 1
    if count == 1:
        print("Alice")
    else:
        print("Bob")