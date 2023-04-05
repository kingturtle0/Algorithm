def backt(n):
    global ans
    if n == N:
        ans += 1
        return

    for i in range(N):
        if v1[i] == 0 and v2[n + i] == 0 and v3[(n - i) + (N - 1)] == 0:
            v1[i] = 1
            v2[n + i] = 1
            v3[(n - i) + (N - 1)] = 1
            backt(n + 1)
            v1[i] = 0
            v2[n + i] = 0
            v3[(n - i) + (N - 1)] = 0

N = int(input())

ans = 0
v1 = [0]*N
v2 = [0]*(2*N-1)
v3 = [0]*(2*N-1)
backt(0)
print(ans)