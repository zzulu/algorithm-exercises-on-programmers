def solution(N, stages):
    result = {}
    reached = len(stages)
    for n in range(1, N+1):
        if reached:
            count = stages.count(n)
            result[n] = count/reached
            reached -= count
        else:
            result[n] = 0
    return sorted(result, key=lambda s: result[s], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) #=> [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4])) #=> [4, 1, 2, 3]
