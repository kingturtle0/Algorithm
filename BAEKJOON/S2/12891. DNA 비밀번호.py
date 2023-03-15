import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dnas = input()
min_cnts = list(map(int, input().split()))

dna_dic = {'A':0, 'C':1, 'G':2, 'T':3}
dna_cnts = [0]*4
ans = 0

def pwdadd(s):
    dna_cnts[dna_dic[s]] += 1

def pwdminus(s):
    dna_cnts[dna_dic[s]] -= 1

def ispwd(lst):
    ret = 0
    for i in range(4):
        if lst[i] >= min_cnts[i]:
            ret += 1

    if ret == 4:
        return 1

    return 0

for i in range(M):
    pwdadd(dnas[i])

if ispwd(dna_cnts):
    ans += 1

for i in range(M, N):
    pwdadd(dnas[i])
    pwdminus(dnas[i-M])
    if ispwd(dna_cnts):
        ans += 1

print(ans)