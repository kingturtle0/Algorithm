def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
    
    mx1 = max(sizes, key=lambda x: x[0])[0]
    mx2 = max(sizes, key=lambda x: x[1])[1]
    
    return mx1 * mx2
