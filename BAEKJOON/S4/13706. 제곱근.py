N = int(input())
s = 1
e = N

while True:
    mid = (s + e) // 2
    if mid ** 2 > N:
        e = mid - 1
    elif mid ** 2 < N:
        s = mid + 1
    else:
        print(mid)
        break