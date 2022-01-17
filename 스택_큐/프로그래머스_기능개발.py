import math

def solution(progresses, speeds):
    answer = []
    times = []
    for i in range(len(progresses)):
        time = math.ceil((100-progresses[i]) / speeds[i])
        times.append(time)

    cnt = 1
    for i in range(1, len(times)):
        if times[i] <= times[i-1]:
            cnt += 1
            times[i] = times[i-1]
        else:
            answer.append(cnt)
            cnt = 1
            
    answer.append(cnt)

    return answer