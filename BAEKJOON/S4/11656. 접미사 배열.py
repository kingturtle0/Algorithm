S = input()
n = len(S)
suffixs = [S[i:n] for i in range(n)]
suffixs.sort()
for suffix in suffixs:
    print(suffix)