def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0 for _ in range(bridge_length)]
    bridge_weight = 0
    
    while truck_weights:
        bridge_weight -= on_bridge.pop(0)
        if bridge_weight + truck_weights[0] <= weight:
            truck_weight = truck_weights.pop(0)
            on_bridge.append(truck_weight)
            bridge_weight += truck_weight
        else:
            on_bridge.append(0)

        answer += 1
        
    answer += bridge_length
    
    return answer