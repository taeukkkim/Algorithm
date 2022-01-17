def solution(triangle):
    for i in range(len(triangle)-1):
        for j in range(i+2):
            if j == 0:
                triangle[i+1][j] += triangle[i][0]
            elif i+1 == j:
                triangle[i+1][j] += triangle[i][-1]
            else:
                triangle[i+1][j] += max(triangle[i][j], triangle[i][j-1])
                
    answer = max(triangle[-1])
    
    return answer