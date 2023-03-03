N = int(input())
arr = [0]*1001

s = 1001
e = 0
for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H
    s = min(s, L)
    e = max(e, L)

mid = arr.index(max(arr))

num = arr[s]
for i in range(s, mid):
    if arr[i] >= arr[i+1]:
        arr[i+1] = num
    else:
        num = arr[i+1]

num = arr[e]
for i in range(e, mid, -1):
    if arr[i] >= arr[i-1]:
        arr[i-1] = num
    else:
        num = arr[i-1]

print(sum(arr))