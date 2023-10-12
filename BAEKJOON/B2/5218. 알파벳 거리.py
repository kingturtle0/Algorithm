T = int(input())
for _ in range(T):
    a, b = input().split()
    length = len(a)
    distances = []
    for i in range(length):
        diff = ord(b[i]) - ord(a[i])
        if diff >= 0:
            distances.append(diff)
        else:
            distances.append(26 + diff)

    print(f'Distances:', *distances)