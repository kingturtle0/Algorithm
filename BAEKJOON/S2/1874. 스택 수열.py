N = int(input()) # 자연수의 크기

lst = [int(input()) for _ in range(N)] # 수열

n = flag = 1
stack = []
pp = []
for i in range(N):          # 수열을 돌면서
    if lst[i] >= n:         # 수열의 값이 오름차순의 자연수보다 크면
        while lst[i] >= n:  # 수열의 값 이하의 모든 값들을 저장하고
            stack.append(n) # push이므로 +를 저장해준다.
            pp.append("+")
            n += 1          # 자연수를 오름차순으로 증가시켜준다.
        stack.pop()         # 수열의 값과 같아질 때까지 반복하므로 마지막 수는 pop
        pp.append("-")      # pop하면 -를 저장해준다.
    else:                   # 수열의 값이 자연수보다 작으면
        num = stack.pop()   # 마지막으로 저장된 값을 pop하고
        if num <= lst[i]:   # pop한 값이 현재 수열의 값보다 작거나 같으면 OK
            pp.append("-")
        else:               # 현재 수열의 값보다 크면 만들 수 없는 수열이므로
            print("NO")     # NO 출력하고 종료
            flag = 0
            break

if flag:
    print(*pp, sep='\n')