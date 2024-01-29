def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    score = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == a[i]:
            score[0] += 1
        if answers[i] == b[i]:
            score[1] += 1
        if answers[i] == c[i]:
            score[2] += 1
    for i in range(3):
        if score[i] == max(score):
            answer.append(i + 1)
    return answer

# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result