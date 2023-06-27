from collections import deque


def bfs():
    q = deque()
    v = [0] * 1000001

    q.append(N)
    v[N] = 1

    while q:
        c = q.popleft()

        for n in (c - 1, c + 1, c * 2):
            if 0 <= n < 1000001 and v[n] == 0:
                if n == K:
                    return v[c]
                q.append(n)
                v[n] = v[c] + 1


N, K = map(int, input().split())

if N < K:
    ans = bfs()
else:
    ans = N - K
print(ans)