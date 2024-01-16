def solution(n):
    sqrtn = n ** 0.5
    if sqrtn - int(sqrtn) > 0:
        return -1
    else:
        return (sqrtn + 1) ** 2
