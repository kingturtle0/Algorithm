def dfs(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == len(blst):
            asm = bsm= 0
            for i in range(N//2):
                for j in range(N//2):
                    if i != j:
                        asm += arr[alst[i]][alst[j]]
                        bsm += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asm - bsm))
        return

    dfs(n + 1, alst + [n], blst)
    dfs(n + 1, alst, blst + [n])



T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 21e8
    dfs(0, [], [])
    print(f'#{test_case} {ans}')