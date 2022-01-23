import heapq

def solution(operations):
    answer = []
    h = []
    max_h = []
    
    for oper in operations:
        oper = oper.split()
        
        if oper[0] == 'I':
            num = int(oper[1])
            heapq.heappush(h, num)
            heapq.heappush(max_h, (-num, num))
        elif not h:
            pass
        elif oper[1] == '1':
            max_value = heapq.heappop(max_h)
            h.remove(max_value[1])
        else:
            min_value = heapq.heappop(h)
            max_h.remove((-min_value,min_value))
            
    if not h:
        return [0, 0]

    return [max_h[0][1], h[0]]