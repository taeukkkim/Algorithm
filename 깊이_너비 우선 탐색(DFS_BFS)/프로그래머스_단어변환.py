from collections import deque

def check(start, word):
    cnt = 0
    for i in range(len(word)):
        if word[i] != start[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    q = deque()
    q.append([begin,[]])
    while True:
        start, visited = q.popleft()
        
        for word in words:
            if word not in visited and check(start, word):
                if word == target:
                    return len(visited) + 1
                temp = visited.copy()
                temp.append(word)
                q.append([word, temp])

    return answer