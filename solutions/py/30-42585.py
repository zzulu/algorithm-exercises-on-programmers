def solution(arrangement):
    count = 0
    stack = []
    for index in range(len(arrangement)):
        if arrangement[index] == '(':
            stack.append(arrangement[index])
        else:
            stack.pop()
            if arrangement[index-1] == ')':
                count += 1
            else:
                count += len(stack)

    return count


print(solution('()(((()())(())()))(())')) # 17
