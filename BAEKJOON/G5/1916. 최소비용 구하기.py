import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    arr[s].append([e, w])
start, end = map(int, input().split())
INF = int(1e9)
lst = [INF] * (N + 1)

def dijk(st):
    hq = []
    heapq.heappush(hq, (0, st))
    lst[st] = 0

    while hq:
        dist, c = heapq.heappop(hq)
        if lst[c] < dist: continue
        for n in arr[c]:
            ndist = dist + n[1]
            if ndist < lst[n[0]]:
                lst[n[0]] = ndist
                heapq.heappush(hq, [ndist, n[0]])

dijk(start)
print(lst[end])