def solution(n, times):
    min_time = 0
    max_time = max(times) * n
    
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        checked = 0
        
        for time in times:
            checked += mid_time // time
            if checked >= n:
                break
        
        if checked >= n:
            answer = mid_time
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
            
    return answer