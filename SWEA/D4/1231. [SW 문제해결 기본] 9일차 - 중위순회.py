def inorder(i):
    global ans
    if i:
        inorder(cl[i])
        ans += arr[i]
        inorder(cr[i])
    return

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    cr = [0] * (N+1)
    cl = [0] * (N+1)
    arr = [''] * (N+1)
    for i in range(N):
        lst = list(input().split())
        arr[int(lst[0])] = lst[1]
        if len(lst) == 4:
            c1 = int(lst[2])
            c2 = int(lst[3])
            cl[c1//2] = c1
            cr[c2//2] = c2
        elif len(lst) == 3:
            c = int(lst[2])
            cl[c//2] = c

    ans = ''
    inorder(1)

    print(f'#{test_case}', ans)