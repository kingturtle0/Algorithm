def solution(n):
    answer = 1
    for i in range(1, n // 2 + 2):
        temp = i
        for j in range(i + 1, n // 2 + 2):
            temp += j
            if temp == n:
                answer += 1
            elif temp > n:
                break
    return answer

# def solution(n):
#     return len([i for i in range(1, n + 1, 2) if n % i == 0])