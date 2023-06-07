N = int(input())
lst = list(map(int, input().split()))
result = []

for i in range(N - 1, -1, -1):
    result.insert(lst[i], N)
    N -= 1

print(*result)
