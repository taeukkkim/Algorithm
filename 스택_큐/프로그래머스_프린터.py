def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]
    
    while True:
        q = queue.pop(0)
        if queue:
            max_p = max([i[1] for i in queue])
        else:
            pass
        
        if q[1] < max_p:
            queue.append(q)
        else:
            answer += 1
            if q[0] == location:
                return answer