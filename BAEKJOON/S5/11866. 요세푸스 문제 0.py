N, K = map(int, input().split())
q = [i for i in range(1, N + 1)]

lst = []
cnt = 0
while q:
    c = q.pop(0)
    cnt += 1

    if cnt == K:
        lst.append(c)
        cnt = 0
    else:
        q.append(c)

print("<", end="")
print(*lst, sep=", ", end="")
print(">")