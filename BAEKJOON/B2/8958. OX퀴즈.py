N = int(input())
for _ in range(N):
    quizs = input()
    ans, run = 0, 0
    for quiz in quizs:
        if quiz == 'O':
            run += 1
        else:
            run = 0
        ans += run

    print(ans)