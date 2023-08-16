import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = dict()
for _ in range(N):
    S[input().strip()] = 1

ans = 0
for _ in range(M):
    if S.get(input().strip()) == 1:
        ans += 1

print(ans)