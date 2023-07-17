import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(heap, x)
    else:
        ans = 0
        if heap:
            ans = heapq.heappop(heap)

        print(ans)