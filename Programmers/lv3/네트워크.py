def dfs(i, n, computers, v):
    v[i] = 1
    for j in range(n):
        if i != j and computers[i][j] == 1 and v[j] == 0:
            dfs(j, n, computers, v)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i, n, computers, visited)
            answer += 1
    
    return answer