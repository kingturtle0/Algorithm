def bfs(st):
    q = []
    visited[st] = 1

    q.append(st)
    ret = st

    while q:
        c = q.pop(0)

        if visited[ret] < visited[c] or (visited[ret] == visited[c] and ret < c):
            ret = c

        for n in arr[c]:
            if visited[n] == 0:
                q.append(n)
                visited[n] = visited[c] + 1

    return ret

T = 10

for test_case in range(1, T + 1):
    N, start = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[] for _ in range(101)]
    visited = [0]*101

    for i in range(0, N, 2):
        arr[lst[i]].append(lst[i+1])

    ans = bfs(start)

    print(f'#{test_case}', ans)