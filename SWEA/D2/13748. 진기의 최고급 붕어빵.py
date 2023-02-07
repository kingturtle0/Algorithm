T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))

    for y in range(N-1):
        for x in range(y+1, N):
            if people[y] > people[x]:
                people[y], people[x] = people[x], people[y]

    flag = 1
    for i in range(N):
        bread_cnt = K * (people[i] // M)
        if bread_cnt - i <= 0:
            flag = 0
            break

    if flag:
        result = "Possible"
    else:
        result = "Impossible"

    print(f"#{test_case}", result)