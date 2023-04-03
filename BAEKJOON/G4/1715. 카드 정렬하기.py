import heapq, sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

ans = 0
while len(heap) > 1:
    t1 = heapq.heappop(heap)
    t2 = heapq.heappop(heap)
    ans += t1+t2
    heapq.heappush(heap, t1+t2)

print(ans)