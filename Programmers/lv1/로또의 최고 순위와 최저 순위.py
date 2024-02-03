def solution(lottos, win_nums):
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    a, b = set(lottos), set(win_nums)
    n = len(a & b)
    zeros = lottos.count(0)
    return [rank[n + zeros] , rank[n]]