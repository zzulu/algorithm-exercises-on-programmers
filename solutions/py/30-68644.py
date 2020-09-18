def solution(numbers):
    result = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            number = numbers[i] + numbers[j]
            if number not in result:
                result.append(number)
    result.sort()
    return result


print(solution([2, 1, 3, 4, 1])) #=> [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7])) #=> [2, 5, 7, 9, 12]
