from collections import deque

def bfs(n, computers, i, visited):
    q = deque([i])
    while q:
        node = q.popleft()
        visited[node] = True
        for j in range(n):
            if j != node and computers[node][j] == 1:
                if visited[j] == False:
                    q.append(j)
                    
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            bfs(n, computers, i, visited)
            answer += 1
            
    return answer