import sys
input = sys.stdin.readline

N, M = map(int, input().split())

girl_group = dict()
for _ in range(N):
    team = input().strip()
    n = int(input())
    member = [input().strip() for _ in range(n)]
    girl_group[team] = member

for _ in range(M):
    quiz = input().strip()
    type = int(input())

    if type:
        for key, value in girl_group.items():
            if quiz in value:
                print(key)
                break
    else:
        print(*sorted(girl_group.get(quiz)), sep='\n')