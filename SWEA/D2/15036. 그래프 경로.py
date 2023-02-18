T = int(input())

def dfs(start):
    for i in range(V):
        if arr[start][i] == 1 and visit[i] == 0:
            visit[i] = 1
            dfs(i)

for test_case in range(1, T + 1):
    V, E = map(int, input().split()) # 노드 개수, 간선 개수
    arr = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(E): # 간선 수만큼 인접 행렬에 1 넣기
        y, x = map(int, input().split()) # 인접행렬에 넣을 곳
        arr[y-1][x-1] = 1

    S, G = map(int, input().split()) # 출발지점, 도착지점
    visit = [0]*(V) # 재방문 방지 배열

    visit[S-1] = 1
    dfs(S-1)

    ans = 0
    if visit[G-1] == 1:
        ans = 1
    print(f'#{test_case}', ans)
