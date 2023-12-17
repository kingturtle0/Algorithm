# N = int(input())
# scores = list(map(int, input().split()))

# max_val = -(21e8)
# for score in scores:
#     if max_val < score:
#         max_val = score

# sum_val = 0
# for score in scores:
#     sum_val += score

# ans = (sum_val / max_val) * 100 / N
# print(ans)

N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
print(sum(scores) / max_score * 100 / N)