N = int(input())

lst = [N]

alst = []
ans = 1
idx = 0
for i in range(N+1):
    lst.append(i)

    n = N
    while n >= 0:
        val = lst[idx] - lst[idx+1]
        if val >= 0:
            lst.append(val)
            n = val
            idx += 1
        else:
            break

    if ans < len(lst):
        ans = len(lst)
        alst = lst

    lst = [N]
    idx = 0

print(ans)
print(*alst)