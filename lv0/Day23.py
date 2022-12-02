# 특이한 정렬
#def solution(numlist, n):
#    numlist.sort(reverse=True)
#    return sorted(numlist, key=lambda x:abs(x-n))

def solution(numlist, n):
    return sorted(numlist, key=lambda x:(abs(x-n),-x))

# 등수 매기기
def solution(score):
    answer = [sum(i)/2 for i in score]
    return [sorted(answer, reverse=True).index(i)+1 for i in answer]

# 옹알이 (1)


# 로그인 성공?
# def solution(id_pw, db):
#     if id_pw in db:
#         return "login"
#     else:
#         if id_pw[0] in [i[0] for i in db]:
#             return "wrong pw"
#         else:
#             return "fail"

def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
