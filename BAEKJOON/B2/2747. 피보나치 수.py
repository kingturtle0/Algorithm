N = int(input())

lst = [0, 1]
for _ in range(N - 1):
    lst.append(lst[-1] + lst[-2])

print(lst[N])
