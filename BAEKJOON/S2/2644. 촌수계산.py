n = int(input())
s, e = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
flag = 0
ans = -1

def bfs(start, level):
    global flag, ans
    q = [(start, level)]

    visited[start] = 1

    while q:
        c, level = q.pop(0)

        if c == e:
            flag = 1
            ans = level
            return

        level += 1

        for num in arr[c]:
            if visited[num] == 0:
                visited[num] = 1
                q.append((num, level))


for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


bfs(s, 0)
print(ans)