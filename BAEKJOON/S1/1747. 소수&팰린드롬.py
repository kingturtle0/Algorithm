N = int(input())
mx = int(1003001)
arr = [0, 0] + [1]*(mx + 1)

for i in range(2, int(mx**0.5) + 1):
    if arr[i]:
        for j in range(i + i, mx + 1, i):
            arr[j] = 0

for i in range(N, mx + 1):
    if arr[i] and str(i) == str(i)[::-1]:
        print(i)
        break