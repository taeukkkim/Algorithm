import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while (scoville[0] < K) and (len(scoville) > 1):
        pop1 = heapq.heappop(scoville)
        pop2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville, pop1 + pop2 * 2)
        
        answer += 1
        
        if (len(scoville) < 2) and (scoville[0] < K):
            return -1
        
    return answer