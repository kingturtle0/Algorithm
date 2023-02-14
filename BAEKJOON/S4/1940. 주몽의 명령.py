import sys
input = sys.stdin.readline

N = int(input()) # 재료 개수
M = int(input()) # 2개의 재료를 합쳐서 갑옷 완성시킬 수 있는 값
materials = list(map(int, input().split())) # 재료 번호 리스트
materials.sort() # 리스트 정렬

start, cnt = 0, 0 # 시작과 합칠 수 있는 재료의 개수 0으로 초기화
end = N - 1 # 종료는 리스트 마지막 인덱스로 초기화

while start < end: # 반복은 시작이 종료보다 작은 동안
    if materials[start] + materials[end] < M: # 투 포인터의 합이 타겟값보다 작은 경우는
        start += 1 # 시작을 1 증가시켜서 큰 값으로 이동 시키기
    elif materials[start] + materials[end] > M: # 큰 경우는
        end -= 1 # 종료를 1 감소시켜서 작은 값으로 이동 시키기
    else: # 타겟값과 같아지면 개수를 1 증가시키고 시작과 종료 모두 이동시키기
        cnt += 1
        start += 1
        end -= 1

print(cnt) # 출력