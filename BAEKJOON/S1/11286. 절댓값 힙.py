import sys
input = sys.stdin.readline

from queue import PriorityQueue
N = int(input())
q = PriorityQueue()

for _ in range(N):
    n = int(input())
    if n:
        q.put((abs(n), n))
    else:
        if q.empty():
            print(0)
        else:
            print(q.get()[1])