T = int(input())

for test_case in range(1, T + 1):
    A, B = input().split()
    lena = len(A)
    lenb = len(B)

    i = j = 0
    cnt = 0
    while i < lena:
        if A[i] != B[j]:
            cnt += 1
            i += 1
        else:
            i += 1
            j += 1
            if j == lenb:
                j = 0
                cnt += 1

    print(f'#{test_case}', cnt)