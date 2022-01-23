from collections import deque, defaultdict

def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)
    
    for win, lose in results:
        win_graph[win].add(lose)
        lose_graph[lose].add(win)

    for i in range(1, n+1):
        for win in lose_graph[i]:
            win_graph[win].update(win_graph[i])
        for lose in win_graph[i]:
            lose_graph[lose].update(lose_graph[i])
    
    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            answer += 1
            
    return answer