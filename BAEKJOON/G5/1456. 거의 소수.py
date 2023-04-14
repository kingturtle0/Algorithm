A, B = map(int, input().split())
N = int(B**(0.5))
arr = [0, 0] + [1] * (N - 1)

for i in range(2, int(N**(0.5)) + 1):
    if arr[i]:
        for j in range(i + i, N + 1, i):
            arr[j] = 0

ans = 0
for i in range(2, N + 1):
    if arr[i]:
        j = i*i
        while j <= B:
            if j >= A:
                ans += 1
            j *= i

print(ans)