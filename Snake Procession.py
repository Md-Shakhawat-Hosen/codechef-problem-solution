t = int(input())
for i in range(t):
    n = int(input())
    s = input().strip()
    li = list(s)
    li1 = []
    for i in range(n):
        if li[i] != '.':
            li1.append(li[i])
    if len(li1) == 0:
        print("Valid")
    if li1[0] == 'T':
        print("Invalid")
    if len(li1) % 2 != 0:
        print("Invalid")
    flag = False
    for i in range(0,len(li1),2):
        if li1[i] == li1[i + 1]:
            flag = True
    if flag:
        print("Invalid")
    else:
        print("Valid")

