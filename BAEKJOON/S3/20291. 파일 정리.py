import sys
input = sys.stdin.readline

dic = dict()
for _ in range(int(input())):
    extension = input().rstrip().split('.')[1]
    if extension in dic:
        dic[extension] +=1
    else:
        dic[extension] = 1

for key, value in sorted(dic.items(), key=lambda x: x[0]):
    print(key, value)