import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sarr = [0]*N
carr = [0]*M
answer = 0

sarr[0] = arr[0]
for i in range(1, N):
    sarr[i] += sarr[i-1] + arr[i]


for i in range(N):
    remainder = sarr[i]%M
    if remainder == 0:
        answer += 1
    carr[remainder] += 1

for i in range(M):
    ci = carr[i]
    answer += (ci*(ci-1))//2

print(answer)
