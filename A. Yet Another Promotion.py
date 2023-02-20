t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    n,m = map(int,input().split())
    if n <= m:
        print(n*min(a,b))
    elif m*a <= (m+1)*b:
        t1 = n // (m+1)
        t2 = n % (m+1)
        t3 = t1*m*a
        t3 = t3+t2*min(a,b)
        print(t3)
    else:
        print(n*b)

