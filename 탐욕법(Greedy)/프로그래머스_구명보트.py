from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))

    while people:
        if people[0] + people[-1] <= limit and len(people) > 1:
            people.pop()
        people.popleft()
        answer += 1
        
    return answer