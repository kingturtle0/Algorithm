import heapq

N = int(input())
pheap = []
mheap = []
cnt0 = 0
cnt1 = 0

for _ in range(N):
    n = int(input())
    if n == 0:
        cnt0 += 1
    elif n == 1:
        cnt1 += 1
    elif n > 0:
        heapq.heappush(pheap, n*(-1))
    else:
        heapq.heappush(mheap, n)

ans = 0
while len(pheap) > 1:
    a = heapq.heappop(pheap)
    b = heapq.heappop(pheap)
    ans += a * b

if len(pheap) == 1:
    ans += heapq.heappop(pheap)*(-1)

while len(mheap) > 1:
    a = heapq.heappop(mheap)
    b = heapq.heappop(mheap)
    ans += a * b

if len(mheap) == 1 and cnt0 == 0:
    ans += heapq.heappop(mheap)

ans += cnt1
print(ans)