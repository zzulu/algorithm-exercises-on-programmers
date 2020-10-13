def solution(n):
    answer, i = 0, 0
    while n >= 3**i:
        i += 1
    while n:
        i -= 1
        n, r = n // 3, n % 3
        answer += r*(3**i)
    return answer


print(solution(45)) #=> 7
print(solution(125)) #=> 229
