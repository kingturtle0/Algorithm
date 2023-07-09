import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_dic = dict()
for _ in range(N+M):
    name = input()
    if name in name_dic:
        name_dic[name] += 1
    else:
        name_dic[name] = 1

results = []
for name, cnt in name_dic.items():
    if cnt == 2:
        results.append(name)

results.sort()
print(len(results))
for result in results:
    print(result, end="")