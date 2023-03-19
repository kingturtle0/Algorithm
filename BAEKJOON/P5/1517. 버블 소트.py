import sys
input = sys.stdin.readline


def mergesort(s, e):
    global ans
    if s + 1 > e:
        return

    m = (s + e) // 2
    mergesort(s, m)
    mergesort(m + 1, e)

    for i in range(s, e + 1):
        lst2[i] = lst[i]

    idx = s
    left = s
    right = m + 1
    while left <= m and right <= e:
        if lst2[left] > lst2[right]:
            lst[idx] = lst2[right]
            ans += right - idx
            right += 1
        else:
            lst[idx] = lst2[left]
            left += 1
        idx += 1

    while left <= m:
        lst[idx] = lst2[left]
        left += 1
        idx += 1

    while right <= e:
        lst[idx] = lst2[right]
        right += 1
        idx += 1

N = int(input())
lst = list(map(int, input().split()))
lst2 = [0]*N
ans = 0

mergesort(0, N - 1)
print(ans)