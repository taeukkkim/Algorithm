def solution(citations):
    length = len(citations)
    citations.sort()
    
    for i in range(length):
        if citations[length-1-i] <= i:
            return i
        
    return length