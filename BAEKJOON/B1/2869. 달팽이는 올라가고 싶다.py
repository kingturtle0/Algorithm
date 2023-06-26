A, B, V = map(int, input().split())
if A == V:
    print(1)
else:
    ans = (V - B) / (A - B)
    if ans - int(ans) > 0:
        print(int(ans) + 1)
    else:
        print(int(ans))