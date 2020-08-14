def solution(n):
    return [int(c) for c in str(n)][::-1]


print(solution(12345)) #=> [5, 4, 3, 2, 1]
