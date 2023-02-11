T = int(input())

def kill(arr, y, x, m):
    total = 0
    for i in range(m):
        for j in range(m):
            total += arr[i+y][j+x]
    return total

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_val = -(21e8)
    for i in range(n-m+1):
        for j in range(n-m+1):
            ret = kill(arr, i, j, m)
            if max_val < ret:
                max_val = ret

    print(f"#{test_case}", max_val)