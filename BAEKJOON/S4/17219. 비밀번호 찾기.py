import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pwd_dict = dict()

for _ in range(N):
    site, pwd = input().split()
    if site in pwd_dict: continue
    pwd_dict[site] = pwd

for _ in range(M):
    target = input().rstrip()
    print(pwd_dict.get(target))