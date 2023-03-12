N = int(input())
lst = list(map(int, input().split()))

# for i in range(1, N):
#     for j in range(i - 1, -1, -1):
#         if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]

for i in range(1, len(lst)):
    idx = i
    val = lst[i]
    for j in range(i - 1, -1, -1):
        if lst[j] < lst[idx]:
            idx = j + 1
            break
        if j == 0:
            idx = 0

    for j in range(i, idx, -1):
        lst[j] = lst[j - 1]
    lst[idx] = val

for i in range(N - 1):
    lst[i + 1] += lst[i]

print(sum(lst))