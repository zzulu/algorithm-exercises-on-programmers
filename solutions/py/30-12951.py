def solution(s):
    result, first = '', True
    for char in s:
        if char != ' ':
            if first:
                result += char.upper()
                first = False
            else:
                result += char.lower()
        else:
            result += char
            first = True
    return result


print(solution('3people unFollowed me')) #=> '3people Unfollowed Me'
print(solution('for the last week')) #=> 'For The Last Week'
