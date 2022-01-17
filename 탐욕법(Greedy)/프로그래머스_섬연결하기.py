def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    connected = set([costs[0][0]])

    while len(connected) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in connected) and (cost[1] in connected):
                continue
            if (cost[0] in connected) or (cost[1] in connected):
                answer += cost[2]
                connected.update([cost[0], cost[1]])
                costs.pop(i)
                break

    return answer