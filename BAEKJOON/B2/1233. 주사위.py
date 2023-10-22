S_1, S_2, S_3 = map(int, input().split())
lst = [0] * (S_1 + S_2 + S_3 + 1)
for i in range(1, S_1 + 1):
    for j in range(1, S_2 + 1):
        for k in range(1, S_3 + 1):
            lst[i + j + k] += 1

print(lst.index(max(lst)))