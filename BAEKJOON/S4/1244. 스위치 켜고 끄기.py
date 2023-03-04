N = int(input())
arr = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    s, c = map(int, input().split())

    if s == 1:
        for i in range(N):
            if (i+1)%c == 0:
                arr[i] = 1 - arr[i]
    else:
        i = j = c - 1
        while True:
            if i < 0 or j > N - 1 or arr[i:j+1] != arr[i:j+1][::-1]:
                i += 1
                j -= 1
                break

            i -= 1
            j += 1

        arr[i:j+1] = [1 - n for n in arr[i:j+1]]

for i in range(1, N+1):
    if i % 20 == 0:
        print(arr[i - 1])
    else:
        print(arr[i - 1], end=' ')
