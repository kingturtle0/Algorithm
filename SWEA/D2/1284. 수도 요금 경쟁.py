T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    
    a_price = P * W
    b_price = Q if W <= R else Q + (W - R) * S
    if a_price <= b_price:
        print(f'#{test_case} {a_price}')
    else:
        print(f'#{test_case} {b_price}')
