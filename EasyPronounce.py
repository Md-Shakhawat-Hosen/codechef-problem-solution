t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    c = 0
    m = 0
    for i in range(len(s)):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            c = 0
        else:
            c = c + 1
            if c >= 4:
                m = c

    if m >= 4:
        print("NO")
    else:
        print("YES")

