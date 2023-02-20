T = int(input())
for x in range(0,T):
    a,b = map(int,input().split())
    if a == b:
        print("NO")
    elif ((a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0)):
        if abs(a-b) == 2:
            print("YES")
        else:
            print("NO")
    elif abs(a - b) == 1 and max(a,b) % 2 == 0:
        print("YES")
    else:
        print("NO")