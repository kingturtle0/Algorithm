def order(n):
    global ans
    if n:
        ans += 1
        order(cl[n])
        order(cr[n])
    return

T = int(input())

for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    cl = [0]*(E+2)
    cr = [0]*(E+2)

    for i in range(E):
        p ,c = arr[i*2], arr[i*2+1]
        if cl[p] == 0:
            cl[p] = c
        else:
            cr[p] = c

    ans = 0
    order(N)    

    print(f'#{test_case}', ans)