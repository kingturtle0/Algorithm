N = int(input())
arr = [list(input().split()) for _ in range(N)]
arr.sort(key=lambda x:int(x[0]))
for lst in arr:
    print(*lst)
