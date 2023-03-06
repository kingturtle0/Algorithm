N, L = map(int, input().split())
arr = [[0]*3] + [[] for _ in range(N)] + [[L, 0, 0]]

for i in range(1, N + 1):
    arr[i] = list(map(int, input().split()))

ans = 0
for i in range(1, N + 2):
    D, R, G = arr[i]
    ans += D - arr[i-1][0]
    val = ans % (R + G) if (R + G) else 0
    if val <= R:
        ans += R - val

print(ans)