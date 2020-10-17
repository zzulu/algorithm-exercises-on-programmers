import functools


def solution(numbers):
    numbers = list(map(str, numbers))
    return str(int(''.join(sorted(numbers, key=functools.cmp_to_key(lambda a, b: int(b+a)-int(a+b))))))


print(solution([6, 10, 2])) #=> '6210'
print(solution([3, 30, 34, 5, 9])) #=> '9534330'
print(solution([40, 403])) #=> 40403
print(solution([45, 453])) #=> 45453
print(solution([40, 404])) #=> 40440
print(solution([44, 404])) #=> 44404
print(solution([3054, 305])) #=> 3054305
print(solution([340, 3403])) #=> 3403403
