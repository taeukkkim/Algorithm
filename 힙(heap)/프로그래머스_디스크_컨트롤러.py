
'''
while문 밖에서 heapq에 jobs를 담고 갱신하지 않는 경우에는 단순히 작업 소요시간만으로 
정렬되어 있어서 이전 작업의 종료시간보다 작업 요청 시점이 뒤에 있는 경우에는 
작업 소요시간이 더 긴 작업이 지금 당장 시작할 수 있더라도 시작하지 않게 됩니다.
따라서 while문을 도는 도중에 이전 작업의 종료시간보다 작업 요청 시점이 더 빠른 작업들만 
heapq에 담아 정렬해 줍니다.
'''
import heapq

def solution(jobs):
    answer, end, i = 0, 0, 0
    start = -1 
    h = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(h, [job[1], job[0]])
                
        if len(h) > 0:
            cur = heapq.heappop(h)
            start = end
            end += cur[0]
            answer += end - cur[1]
            i +=1
        else:
            end += 1
                
    return answer // len(jobs)