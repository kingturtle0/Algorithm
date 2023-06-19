import sys
input = sys.stdin.readline


def rounding(n):
    inte = int(n)
    deci = n - inte
    if deci < 0.5:
        return inte
    else:
        return inte + 1


n = int(input())
lst = sorted([int(input()) for _ in range(n)])
num = rounding(n*0.15)
if n:
    print(rounding(sum(lst[num:n-num])/(n-num*2)))
else:
    print(0)
