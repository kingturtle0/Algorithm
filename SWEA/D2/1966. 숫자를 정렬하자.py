T = int(input())# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    num = list(map(int, input().split()))
    result = sorted(num)
    
    print(f'#{test_case}', end = ' ')
    for i in range(length):
        print(result[i], end = ' ')
    print()
