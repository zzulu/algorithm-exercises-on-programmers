def solution(prices):
    result = []
    length = len(prices)
    for start in range(length):
        end = start
        while end < length-1:
            end += 1
            if prices[start] > prices[end]:
                break
        result.append(end-start)
    return result


print(solution([1, 2, 3, 2, 3])) #=> [4, 3, 1, 1, 0]
