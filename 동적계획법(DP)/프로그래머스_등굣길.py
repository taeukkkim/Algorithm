def solution(m, n, puddles):
    map = [[0]*(m) for _ in range(n)]
    map[0][0] = 1
    puddles = [[x-1,y-1] for x,y in puddles]
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if [i,j] in puddles:
                map[j][i] = 0
            else:
                map[j][i] = map[j-1][i] + map[j][i-1]

    return map[-1][-1] % 1000000007