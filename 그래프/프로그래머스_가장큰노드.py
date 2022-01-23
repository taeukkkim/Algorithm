from collections import deque, defaultdict

def solution(n, edge):
    distance = [-1] * (n+1)
    graph = defaultdict(list)
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    q = deque([1])
    distance[0] = 0

    while q:
        now = q.popleft()
        
        for node in graph[now]:
            if distance[node-1] == -1:
                q.append(node)
                distance[node-1] = distance[now-1] + 1

    return distance.count(max(distance))