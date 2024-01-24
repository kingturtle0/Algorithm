# from collections import defaultdict

# def solution(nums):
#     types = defaultdict(int)
#     for num in nums:
#         types[num] += 1
#     return min(len(nums) // 2, len(types))

def solution(nums):
    return min(len(nums) // 2, len(set(nums)))