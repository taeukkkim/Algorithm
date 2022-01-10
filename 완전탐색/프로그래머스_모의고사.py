def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0] * 3

    for i, ans in enumerate(answers):
        if pattern1[i % len(pattern1)] == ans:
            scores[0] += 1
        if pattern2[i % len(pattern2)] == ans:
            scores[1] += 1
        if pattern3[i % len(pattern3)] == ans:
            scores[2] += 1
            
    answer = [i+1 for i in range(3) if scores[i] == max(scores)]
    
    return answer