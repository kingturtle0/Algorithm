import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = []
    for idx, value in enumerate(list(map(int, input().split()))):
        lst.append((idx, value))

    idx = 0
    while True:
        importance = lst[idx]
        for i in range(idx + 1, N):
            if importance[1] < lst[i][1]:
                lst.pop(idx)
                lst.append(importance)
                break
        else:
            idx += 1
            if idx == N:
                break

    for i in range(N):
        if lst[i][0] == M:
            print(i + 1)
            break