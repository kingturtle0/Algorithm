N = int(input())
lst = [int(input()) for _ in range(N)]

for i in range(N, 0, -1):
    for j in range(1, i):
        if lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]

print(*lst, sep='\n')