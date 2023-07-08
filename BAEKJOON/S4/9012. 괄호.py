T = int(input())
for _ in range(T):
    vps = input()
    stack = []
    ans = "YES"
    for p in vps:
        if p == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                ans = "NO"
                break

    if stack:
        ans = "NO"

    print(ans)