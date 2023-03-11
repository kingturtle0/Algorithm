num = list(input())
n = len(num)

for i in range(n):
    for j in range(i + 1, n):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]

print(''.join(num))