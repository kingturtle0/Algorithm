T = int(input())

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())

    result_h = h1 + h2
    result_m = m1 + m2

    if result_m >= 60:
        result_m -= 60
        result_h += 1

    if result_h > 12:
        result_h -= 12
        
    print(f'#{test_case} {result_h} {result_m}')
