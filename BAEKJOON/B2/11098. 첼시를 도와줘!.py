n = int(input())
for _ in range(n):
    p = int(input())
    players = [input().split()for _ in range(p)]
    ans = max(players, key=lambda x:int(x[0]))[1]
    print(ans)