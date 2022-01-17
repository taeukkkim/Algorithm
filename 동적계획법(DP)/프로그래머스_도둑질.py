def solution(money):
    # 첫 집을 터는 경우
    case1 = [0] * len(money)
    case1[0] = money[0]
    # 첫 집은 안털고 마지막 집을 터는 경우
    case2 = [0] * len(money)
    
    for i in range(1, len(money)): 
        case1[i] = max(case1[i-1], money[i] + case1[i-2])
        case2[i] = max(case2[i-1], money[i] + case2[i-2])

    case1[-1] = 0

    return max(max(case1), max(case2))