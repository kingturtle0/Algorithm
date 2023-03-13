import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

def quicksort(start, end, k):
    if start < end:
        p = pivot(start, end)
        if p == k:
            return
        elif p > k:
            quicksort(start, p - 1, k)
        elif p < k:
            quicksort(p + 1, end, k)

def pivot(start, end):
    if start + 1 == end:
        if lst[start] > lst[end]:
            lst[start], lst[end] = lst[end], lst[start]
        return end

    mid = (start + end) // 2
    lst[start], lst[mid] = lst[mid], lst[start]

    i = start + 1
    j = end
    while i <= j:
        while lst[i] < lst[start] and i < N - 1:
            i += 1

        while lst[j] > lst[start] and j > 0:
            j -= 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    lst[start], lst[j] = lst[j], lst[start]
    return j


quicksort(0, N - 1, K - 1)
print(lst[K - 1])