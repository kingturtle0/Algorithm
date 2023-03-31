import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))
targetN = int(input())
targets = list(map(int, input().split()))

for i in range(targetN):
    ans = 0
    st = 0
    ed = N - 1
    while st <= ed:
        mid = (st + ed) // 2
        if targets[i] > numbers[mid]:
            st = mid + 1
        elif targets[i] < numbers[mid]:
            ed = mid - 1
        else:
            ans = 1
            break

    print(ans)