def solution(n):
    result = 0
    while n:
        n, r = n // 2, n % 2
        result += r
    return result


print(solution(5)) #=> 2
print(solution(6)) #=> 2
print(solution(5000)) #=> 5
