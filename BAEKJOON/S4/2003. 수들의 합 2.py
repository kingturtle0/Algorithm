N, M = map(int, input().split())
numbers = list(map(int, input().split()))

ans = 0
start, end = 0, 1
while True:
    total = sum(numbers[start:end])

    if total < M:
        end += 1
    elif total > M:
        start += 1
    else:
        ans += 1
        end += 1

    if start > end or end > N:
        break

print(ans)