def func(a,b):
    if a == 0:
        return b
    return func(b%a,a)
t = int(input())
for i in range(t):
    apple, orange = map(int, input().split())
    # contestant = 0
    # for i in range(m // 2 + 1, 0, -1):
    #     if apple % i == 0 and orange % i == 0:
    #         contestant = i
    #         break
    #
    # print(contestant)
    r = func(apple,orange)
    print(r)



