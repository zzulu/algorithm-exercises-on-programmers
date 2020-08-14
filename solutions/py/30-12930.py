def solution(s):
    result = ''
    index = 0
    for char in s:
        if char == ' ':
            result += char
            index = 0
        else:
            result += char.lower() if index % 2 else char.upper()
            index += 1
    return result


print(solution('try hello world')) #=> 'TrY HeLlO WoRlD'
