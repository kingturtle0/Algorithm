def solution(n, lost, reserve):
    dup = [l for l in lost if l in reserve]
    for d in dup:
        lost.remove(d)
        reserve.remove(d)
    
    lost.sort()
    reserve.sort()
    for r in reserve:
        if r == 1:
            if 2 in lost:
                lost.remove(2)
        elif r < n:
            if r - 1 in lost:
                lost.remove(r - 1)
            elif r + 1 in lost:
                lost.remove(r + 1)
        else:
            if n - 1 in lost:
                lost.remove(n - 1)
    return n - len(lost)