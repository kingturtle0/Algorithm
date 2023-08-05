from collections import deque
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    q = deque(input().strip()[1:-1].split(','))
    if n == 0:
        q = deque()

    r = 0
    for n in p:
        if n == 'R':
            r += 1
        else:
            if len(q):
                if r % 2:
                    q.pop()
                else:
                    q.popleft()
            else:
                print('error')
                break
    else:
        if r % 2:
            q.reverse()
        print('[' + ','.join(q) + ']')