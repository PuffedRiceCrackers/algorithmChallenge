from collections import deque

def solution(bridge_length, weight, truck_weights):
    if bridge_length == 1:
        return len(truck_weights) + 1
    truck_weights = deque(truck_weights)
    time = 0
    onBridge = deque([])
    while True:
        time += 1
        if not onBridge:
            onBridge.append((truck_weights.popleft(), time))
        else:
            if onBridge[0][1] + bridge_length == time:
                onBridge.popleft()           
            if truck_weights:
                if sum(item[0] for item in onBridge) + truck_weights[0] <= weight:
                    onBridge.append((truck_weights.popleft(), time))            
            else:
                return onBridge[-1][1] + bridge_length


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


print(solution(bridge_length, weight, truck_weights))