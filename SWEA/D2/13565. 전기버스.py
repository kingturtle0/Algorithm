T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))

    stations = [0] * (N+1)
    for i in range(M):
        stations[chargers[i]] = 1

    move_cnt = K
    min_charge = 0
    location = 0
    while location < N:
        if stations[location + move_cnt]:
            location += move_cnt
            min_charge += 1
            move_cnt = K
            if location + move_cnt >= N:
                break
        else:
            move_cnt -= 1

        if (move_cnt == 0) or (N - chargers[-1] > K):
            min_charge = 0
            break

    print(f'#{test_case} {min_charge}')


# other way
T = int(input())

for tc in range(1, T + 1):
    k, n, m = map(int, input().split())

    stations = [0]*(n+1)
    for idx in map(int, input().split()):
        stations[idx] += 1

    cnt = 0
    limit = 0
    location = 0
    while location < n:
        if stations[location+k-limit] == 1:
            location += k - limit
            cnt += 1
            limit = 0
        else:
            limit += 1

        if location+k-limit >= n:
            break

        if limit == k:
            cnt = 0
            break

    print(f'#{tc}', cnt)