L = int(input())
S = input()

ans = 0
for i in range(L):
    ans += (ord(S[i]) - ord('a')+1)*(31**i)

print(ans%1234567891)