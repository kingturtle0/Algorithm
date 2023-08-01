import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = dict()
for i in range(1, N + 1):
    s = input().rstrip()
    dic[s] = i 
    dic[i] = s

for _ in range(M):
    question = input().rstrip()
    if question.isnumeric():
        print(dic.get(int(question)))
    else:
        print(dic.get(question))
