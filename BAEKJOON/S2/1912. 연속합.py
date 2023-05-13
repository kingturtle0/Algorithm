N = int(input())
lst = [0] + list(map(int, input().split()))
result = [0] * (N + 1)

if max(lst[1:]) < 0:
    ans = max(lst[1:])
else:
    for i in range(1, N + 1):
        if result[i - 1] + lst[i] > 0:
            result[i] = result[i - 1] + lst[i]

    ans = max(result)

print(ans)