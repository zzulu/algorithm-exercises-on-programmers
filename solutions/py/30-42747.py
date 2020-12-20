def solution(citations):
    citations.sort()
    for index in range(len(citations)):
        h = len(citations)-index
        if citations[index] >= h:
            return h
    return 0


print(solution([3, 0, 6, 1, 5])) #=> 3
print(solution([0, 0, 0, 0, 0])) #=> 0
