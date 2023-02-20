T = int(input())
for x in range(T):
    maxT, maxN, sumN = map(int,input().split())
    sum = 0
    count = 0
    a = 0
    for i in range(1,maxT+1):
        t = i * maxN
        if t <= sumN:
            sum = sum + maxN*maxN
            count = count + maxN
        elif t > sumN:
            v = sumN - count
            a = v * v
            break

    print(sum+a)

