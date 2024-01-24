def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    answer = [sum(map(lambda x: dic.get(x, 0), p)) for p in photo]
    return answer