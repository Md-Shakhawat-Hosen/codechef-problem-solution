T = int(input())
for x in range(T):
    A, B, A1, B1, A2, B2 = map(int, input().split())
    a_max = max(A,B)
    b_min = min(A,B)

    a1_max = max(A1,B1)
    b1_min = min(A1, B1)

    a2_max = max(A2,B2)
    b2_min = min(A2, B2)


    if a_max == a1_max and b_min == b1_min:
        print(1)
    elif a_max == a2_max and b_min == b2_min:
        print(2)
    else:
        print(0)