# def solution(s):
#     return int(s)

# int() 구현하기
def solution(s):
    numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    result = 0
    for index, char in enumerate(s[::-1]):
        if char == '-':
            result *= -1
        elif char != '+':
            result += numbers[char] * (10**index)

    return result


print(solution('1234'))
print(solution('+1234'))
print(solution('-1234'))
