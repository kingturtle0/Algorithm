def bfs(start, end):
    q = []
    v = [0]*(V+1)

    q.append(start)
    v[start] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
                if v[end] != 0:
                    return v[end] - 1

    return 0

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    S, G = map(int, input().split())

    ans = bfs(S, G)

    print(f'#{test_case}', ans)