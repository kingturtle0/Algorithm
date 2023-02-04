T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    falling = [0] * N
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if box[i] > box[j]:
                cnt += 1
        falling[i] = cnt

    max_val = falling[0]
    for i in range(1, N):
        if falling[i] > max_val:
            max_val = falling[i]

    print(f'#{test_case} {max_val}')