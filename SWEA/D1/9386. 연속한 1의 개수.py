T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    ones = list(map(int, input()))

    for i in range(N-1):
        if ones[i+1] == 1:
            ones[i+1] += ones[i]

    max_cnt = ones[0]
    for i in range(1, N):
        if ones[i] > max_cnt:
            max_cnt = ones[i]

    print(f'#{test_case} {max_cnt}')

T = int(input())

# 더 간단하게
for test_case in range(1, T + 1):
    N = int(input())
    ones = list(map(int, input()))
    max_cnt = cnt = 0
    for i in range(N):
        if ones[i]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 0

    print(f'#{test_case}', max_cnt)