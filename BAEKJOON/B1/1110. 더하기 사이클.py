N = input()
prev = N if int(N) > 9 else '0' + N
new = '100'
ans = 0
while int(new) != int(N):
  new = prev[-1] + str(sum(map(int, prev)))[-1]
  prev = new
  ans += 1

print(ans)