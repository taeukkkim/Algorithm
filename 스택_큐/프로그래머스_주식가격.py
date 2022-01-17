from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        price = prices.popleft()
        sec = 0
        for p in prices:
            sec += 1
            if p < price:
                break
                
        answer.append(sec)
        
    return answer