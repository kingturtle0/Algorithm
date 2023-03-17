import sys
input = sys.stdin.readline

def mergesort(start, end):
    if start + 1 > end:
        return
    mid = (start + end) // 2
    mergesort(start, mid)
    mergesort(mid + 1, end)

    for i in range(start, end + 1):
        ans[i] = lst[i]

    idx = start
    g1 = start
    g2 = mid + 1
    while g1 <= mid and g2 <= end:
        if ans[g1] < ans[g2]:
            lst[idx] = ans[g1]
            g1 += 1
        else:
            lst[idx] = ans[g2]
            g2 += 1
        idx += 1

    while g1 <= mid:
        lst[idx] = ans[g1]
        g1 += 1
        idx += 1

    while g2 <= end:
        lst[idx] = ans[g2]
        g2 += 1
        idx += 1

N = int(input())
lst = [0]*N
for i in range(N):
    lst[i] = int(input())
ans = [0]*N

mergesort(0, N - 1)
print(*lst, sep='\n')
