from collections import deque

N = int(input())
arr = [[] for _ in range(N + 1)]
times = [0]*(N + 1)
prior = [0]*(N + 1)


for i in range(1, N + 1):
    time, *lst = list(map(int, input().split()))
    times[i] = time
    for n in lst:
        if n == -1:
            break
        arr[n].append(i)
        prior[i] += 1

q = deque()
for i in range(1, N + 1):
    if prior[i] == 0:
        q.append(i)

results = times[:]
while q:
    c = q.popleft()

    for i in arr[c]:
        prior[i] -= 1
        results[i] = max(results[i], results[c] + times[i])
        if prior[i] == 0:
            q.append(i)


for result in results[1:]:
    print(result)