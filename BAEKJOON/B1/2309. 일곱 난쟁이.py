lst = [int(input()) for _ in range(9)]
lst.sort()

val = sum(lst)
a, b = 0, 0
for i in range(8):
    for j in range(i+1, 9):
        if val - lst[i] - lst[j] == 100:
            a, b = lst[i], lst[j]
            break

lst.remove(a)
lst.remove(b)

for i in range(7):
    print(lst[i])