# def solution(n, arr1, arr2):
#     answer = []
#     for i in range(n):
#         temp = ""
#         x1 = f"{int(bin(arr1[i])[2:]):0={n}}"
#         x2 = f"{int(bin(arr2[i])[2:]):0={n}}"
#         for j in range(n):
#             if x1[j] == "0" and x2[j] == "0":
#                 temp += " "
#             else:
#                 temp += "#"
#         answer.append(temp)
#     return answer

def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        row = bin(x|y)[2:].rjust(n, "0")
        answer.append(row.replace("1", "#").replace("0", " "))
    return answer