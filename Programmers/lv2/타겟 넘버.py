def dfs(level, value, numbers, target):
    if level == len(numbers):
        if value == target:
            return 1
        return 0
    
    ans1 = dfs(level + 1, value - numbers[level], numbers, target)
    ans2 = dfs(level + 1, value + numbers[level], numbers, target)
    
    return ans1 + ans2


def solution(numbers, target):
    return dfs(0, 0, numbers, target)
