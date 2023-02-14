N = int(input()) # 1 ~ 10,000,000사이의 자연수 입력받기

start = end = 1 # 자연수의 범위로 시작하므로 start와 end를 1로 초기화

# 자기 자신인 경우를 포함해야 하므로 cnt를 1로 초기화, start와 end가 1이므로 합도 1
cnt = total = 1
while end != N: # end가 N이 아닌 동안 반복하기
    if total > N: # 합이 N보다 크면 start를 1 증가시켜서 범위를 줄이기
        total -= start
        start += 1
    elif total < N: # 합이 N보다 작으면 end를 1 증가시켜서 범위를 늘리기
        end += 1
        total += end
    else: # 합이 N과 같으면 cnt 1증가시키고 end를 1 증가시켜서 범위 늘리기
        cnt += 1
        end += 1
        total += end

    if start == (N//2+1): # 더 빠른 종료를 위해 만약 start가 N의 절반을 넘어서면 멈추기
        break

print(cnt)