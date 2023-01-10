T = int(input())

for test_case in range(1, T + 1):
    num_list = list(map(int, input().split()))
    total = sum([i for i in num_list if i % 2])
    print(f"#{test_case} {total}")
