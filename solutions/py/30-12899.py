def solution(n):
    rule = {0: '4', 1: '1', 2:'2'}
    answer = ''
    while n:
        n, r = n // 3, n % 3
        answer = rule[r] + answer
        if not r:
            n -= 1
    return answer


print(solution(1)) #=> 1
print(solution(2)) #=> 2
print(solution(3)) #=> 4
print(solution(4)) #=> 11
print(solution(5)) #=> 12
print(solution(6)) #=> 14
print(solution(7)) #=> 21
print(solution(8)) #=> 22
print(solution(9)) #=> 24
print(solution(10)) #=> 41
