def solution(n):
    return sum([int(d) for d in str(n)])


print(solution(123)) #=> 6
print(solution(987)) #=> 24
