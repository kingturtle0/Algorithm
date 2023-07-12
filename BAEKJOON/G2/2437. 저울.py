# N = int(input())
# lst = [0] + sorted(list(map(int, input().split())))

# acc_lst = [0]*(N + 1)
# acc_lst[1] = lst[1]
# for i in range(2, N + 1):
#     acc_lst[i] = lst[i] + acc_lst[i - 1]

# ans = 0
# for i in range(1, N + 1):
#     if lst[i] <= acc_lst[i - 1] + 1:
#         ans += lst[i]
#     else:
#         break

# print(ans + 1)

N = int(input())
lst = sorted(list(map(int, input().split())))

ans = 1
for i in range(N):
    if ans < lst[i]:
        break
    ans += lst[i]

print(ans)