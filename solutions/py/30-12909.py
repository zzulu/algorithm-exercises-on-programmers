def solution(s):    
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(solution('()()')) #=> true
print(solution('(())()')) #=> true
print(solution(')()(')) #=> false
print(solution('(()(')) #=> false
