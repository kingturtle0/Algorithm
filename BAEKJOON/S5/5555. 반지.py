clue = input()
N = int(input())
ans = 0
for _ in range(N):
    if clue in input() * 2:
        ans += 1

print(ans)