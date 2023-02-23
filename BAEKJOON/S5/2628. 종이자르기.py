rend, cend = map(int, input().split())
n = int(input())

rlst, clst = [0, rend], [0, cend] # 자를 위치를 넣을 리스트

for _ in range(n):
    line, num = map(int, input().split()) # 가로세로와 자를 곳 입력
    if line: # 자를 위치의 반대되는 리스트에 넣어준다.
        rlst.append(num)
    else:
        clst.append(num)

rlst.sort() # 간격을 구해야 하므로 순서에 맞게
clst.sort() # 두 리스트 모두 정렬해주어야한다.

rmax = cmax = -(21e8)
for i in range(len(rlst)-1):
    rlen = rlst[i+1] - rlst[i]
    if rmax < rlen:
        rmax = rlen

for i in range(len(clst)-1):
    clen = clst[i+1] - clst[i]
    if cmax < clen:
        cmax = clen

print(rmax*cmax) # 가로세로로 가장 큰 간격을 곱해주어 면적 출력