import sys, heapq
input = sys.stdin.readline

def dijk(start):
    heapq.heappush(hq, (0, start))

    while hq:
        dist, c = heapq.heappop(hq)
        if dist > lst[c]: continue

        for n in arr[c]:
            ndist = dist + n[1]
            if ndist < lst[n[0]]:
                lst[n[0]] = ndist
                heapq.heappush(hq, (ndist, n[0]))


N, D = map(int, input().split())
arr = [[] for _ in range(D + 1)]
for i in range(D):
    arr[i].append((i + 1, 1))

for _ in range(N):
    s, e, w = map(int, input().split())
    if e > D: continue
    arr[s].append((e, w))

INF = 10000
lst = [INF] * (D + 1)

lst[0] = 0
hq = []
dijk(0)
print(lst[D])