from collections import deque


def solution(priorities, location):
    queue = deque(priorities)
    order = 0
    while priorities:
        for index in range(1, len(queue)):
            if queue[index] > queue[0]:
                queue.rotate(-1)
                break
        else:
            queue.popleft()
            order += 1
            if location == 0:
                break
        location = location - 1 if location else location - 1 + len(queue)
    return order


print(solution([2, 1, 3, 2], 2)) #=> 1
print(solution([1, 1, 9, 1, 1, 1], 0)) #=> 5
