from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N + 1)])

lst = []
cnt = 0
while q:
    c = q.popleft()
    cnt += 1

    if cnt == K:
        lst.append(str(c))
        cnt = 0
    else:
        q.append(c)

print("<", ", ".join(lst), ">", sep="")
