import collections


def weight_sum(bridge):
    weight = 0
    for truck in bridge:
        weight += truck[0]
    return weight


def solution(bridge_length, weight, truck_weights):
    count = 0
    tw = collections.deque(truck_weights)
    bridge = collections.deque()
    while tw or bridge:
        print(bridge, tw, count)
        for truck in bridge:
            truck[1] -= 1

        if bridge and bridge[0][1] == 0:
            bridge.popleft()

        if tw and tw[0] + weight_sum(bridge) <= weight:
            bridge.append([tw.popleft(), bridge_length])

        count += 1

    return count


print(solution(2, 10, [7, 4, 5, 6])) #=> 8
print(solution(100, 100, [10])) #=> 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) #=> 110
