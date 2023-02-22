rend, cend = map(int, input().split())
n = int(input())

rlst, clst = [0, rend], [0, cend]

for _ in range(n):
    line, num = map(int, input().split())
    if line:
        rlst.append(num)
    else:
        clst.append(num)

rlst.sort()
clst.sort()

rmax = cmax = -(21e8)
for i in range(len(rlst)-1):
    rlen = rlst[i+1] - rlst[i]
    if rmax < rlen:
        rmax = rlen

for i in range(len(clst)-1):
    clen = clst[i+1] - clst[i]
    if cmax < clen:
        cmax = clen

print(rmax*cmax)