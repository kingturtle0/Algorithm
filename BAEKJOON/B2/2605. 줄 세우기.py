n = int(input())
orders = [0] + list(map(int, input().split())) # 숫자 맞추기위해 0추가
lst = [0]*(n+1) # 위와 동일한 길이의 숫자 넣을 리스트

for i in range(1, n+1):        # 1번부터 n번까지
    if lst[n-orders[i]] == 0:  # 들어갈 자리가 0이면
        lst[n-orders[i]] = i   # 그냥 해당 자리에 넣기
    else:                      # 들어갈 자리에 숫자가 있으면
        # 집어넣을 자리 앞과 뒤 사이를 잘라서 넣기
        lst = lst[1:(n+1)-orders[i]] + [i] + lst[(n+1)-orders[i]:]

print(*lst[1:]) # 1번부터 출력