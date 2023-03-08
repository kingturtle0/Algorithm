from collections import deque
q = deque([n + 1 for n in range(int(input()))])

while len(q) > 1:
    q.popleft()
    num = q.popleft()
    q.append(num)

print(q[0])