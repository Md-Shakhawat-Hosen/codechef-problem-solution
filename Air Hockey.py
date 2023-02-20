n = int(input())
for x in range(n):
    inp = input().split()
    alice = int(inp[0])
    bob = int(inp[1])
    if (alice+bob) == 0:
        print(7-(alice+bob))
    elif alice > bob:
        print(7-alice)
    elif bob > alice:
        print(7-bob)
    elif alice == bob:
        print(7-alice)
