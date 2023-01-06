T= int(input())
num_list = list(map(int, input().split()))
print(sorted(num_list)[T//2])
