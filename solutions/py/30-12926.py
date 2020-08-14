def solution(s, n):
    result = ''
    for char in s:
        if char != ' ':
            max_range = ord('Z') if char.isupper() else ord('z')
            d = n - 26 if ord(char) + n > max_range else n
            char = chr(ord(char)+d)
        result += char
    return result


print(solution('AB', 1)) #=> 'BC'
print(solution('z', 1)) #=> 'a'
print(solution('a B z', 4)) #=> 'e F d'
