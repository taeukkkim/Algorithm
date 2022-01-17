def solution(N, number):
    dp = [[]]
    for i in range(1,9):
        temp = set()
        for j in range(1,i):
            for k in dp[j]:
                for l in dp[i - j]:
                    temp.add(k + l)
                    if k - l >= 0:
                        temp.add(k - l)
                    temp.add(k * l)
                    if (k != 0) and (l != 0):
                        temp.add(k // l)
        temp.add(int(str(N) * i))
        if number in temp:
            return i
        dp.append(list(temp))
    return -1