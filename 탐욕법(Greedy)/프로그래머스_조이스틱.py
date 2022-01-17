def solution(name):
    answer = 0
    changes = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    i = 0
    
    while True:
        answer += changes[i]
        changes[i] = 0
        
        if sum(changes) == 0:
            break
        
        left = right = 1
        while changes[i-left] == 0:
            left += 1
        while changes[i+right] == 0:
            right += 1
        
        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right
    
    return answer