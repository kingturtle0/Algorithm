from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
q = deque()
for _ in range(N):
    command = input().split()
    c = command[0]
    if c == 'push':
        q.append(command[1])
    elif c == 'pop':
        if q:
            n = q.popleft()
            print(n)
        else:
            print(-1)
    elif c == 'size':
        print(len(q))
    elif c == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)