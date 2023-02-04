T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 카드 개수
    cards = list(map(int, input())) # 카드들 목록
    counts = [0] * 10 # 숫자의 개수

    for i in range(N): # 카드에 적힌 숫자들의 개수 구하기
        counts[cards[i]] += 1

    number = 0
    max_num = counts[0]
    for i in range(1, 10):
        if counts[i] >= max_num: 
            max_num = counts[i] # 가장 많이 나온 숫자 장수
            number = i # 가장 많이 나온 숫자

    print(f'#{test_case} {number} {max_num}')