import sys
input = sys.stdin.readline

N = int(input())
nlst = list(map(int, input().split()))
M = int(input())
mlst = list(map(int, input().split()))

dic = dict()
for i in range(N):
    if nlst[i] in dic:
        dic[nlst[i]] += 1
    else:
        dic[nlst[i]] = 1


for i in range(M):
    ans = dic.get(mlst[i])
    if ans is None:
        ans = 0
    print(ans, end=' ')
