from collections import deque

N = int(input())
q = deque([i for i in range(1, N + 1)])
while q:
    front = q.popleft()
    print(front, end=' ')
    if q:
        back = q.popleft()
        q.append(back)