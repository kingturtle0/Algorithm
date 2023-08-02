from collections import deque


def bfs():
    q = deque()
    q.append([A, 1])
    while q:
        n, cnt = q.popleft()

        if n == B:
            return cnt
        elif n < B:
            q.append([n*2, cnt + 1])
            q.append([int(str(n)+'1'), cnt + 1])

    return -1


A, B = map(int, input().split())
ans = bfs()
print(ans)