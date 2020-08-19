def solution(s):
    numbers = list(map(int, s.split()))
    return '{} {}'.format(min(numbers), max(numbers))


print(solution('1 2 3 4')) #=> '1 4'
print(solution('-1 -2 -3 -4')) #=> '-4 -1'
print(solution('-1 -1')) #=> '-1 -1'
