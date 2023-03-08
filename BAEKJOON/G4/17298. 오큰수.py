N = int(input())
lst = list(map(int, input().split()))

ans = [0]*N
stack = []
for i in range(N):
    while stack and lst[stack[-1]] < lst[i]:
        idx = stack.pop()
        ans[idx] = lst[i]
    stack.append(i)

while stack:
    idx = stack.pop()
    ans[idx] = -1

print(*ans)