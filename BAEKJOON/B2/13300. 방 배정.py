import sys
input = sys.stdin.readline

N, K = map(int, input().split())# 학생 수, 반 최대 인원
arr = [[] for _ in range(12)]   # 성별과 학년따라 12개의 리스트 배열

for i in range(N):              # 학생 수만큼 반복
    s, g = map(int, input().split()) # 성별과 학년 입력받아서
    arr[2*(g-1)+s].append(1)    # 이진트리처럼 각 리스트에 1 넣기

cnt = 0                         # 방 개수
for i in range(12):             # 배열 안의 리스트를 보면서
    nper = len(arr[i])          # 그 리스트의 길이가
    if nper:                    # 0이 아닐 때
        cnt += (nper-1)//K+1    # 최대 인원수로 나눈 몫에 1을 더한 값
                                # 즉, 필요 방 개수를 더해주기
print(cnt)