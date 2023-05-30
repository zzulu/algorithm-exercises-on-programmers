def solution(numbers):
    result, stack = [-1], [numbers[-1]]
    length = len(numbers)
    for i in range(length-2, -1, -1):
        while stack:
            if stack[-1] > numbers[i]:
                result.append(stack[-1])
                stack.append(numbers[i])
                break
            else:
                stack.pop()

        if not stack:
            result.append(-1)
            stack.append(numbers[i])
            continue

    return result[::-1]


print(solution([2, 3, 3, 5])) #=> [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) #=> [-1, 5, 6, 6, -1, -1]
