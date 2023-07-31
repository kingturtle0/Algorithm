N = int(input())
M = int(input())
P = input()

s, e = 0, 0
ans = 0
while e < M:
    if P[e:e + 3] == 'IOI':
        e += 2
        if e - s == 2*N:
            ans += 1
            s += 2
    else:
        e += 1
        s = e

print(ans)