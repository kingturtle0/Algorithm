for _ in range(int(input())):
    total = sum([i for i in range(65, 91)])
    S = set(input())
    for s in S:
        total -= ord(s)
    print(total)