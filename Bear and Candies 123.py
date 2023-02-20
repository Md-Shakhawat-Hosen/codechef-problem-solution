t = int(input())
for i in range(t):
    l,b = map(int,input().split())
    limak = 0
    bob = 0
    i = 1
    while True:
        limak = i*i
        if limak > l:
            print("Bob")
            break

        bob = (i+1)*i
        if bob > b:
            print("Limak")
            break
        i = i + 1




