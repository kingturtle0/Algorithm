T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    result = divmod(a,b)
    print(f"#{test_case} {result[0]} {result[1]}")
