N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = []
for i in range(N):
    cnt = 1
    x, y = arr[i]
    for j in range(N):
        if i == j: continue
        p, q = arr[j]
        if p > x and q > y:
            cnt += 1
    result.append(cnt)

print(*result)