def solution(n):
    tri = ''
    while n:
        tri += str(n % 3)
        n //= 3
    return int(tri, 3)