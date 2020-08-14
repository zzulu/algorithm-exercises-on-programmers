def solution(n, m):
    x = n if n < m else m
    for num in range(x, 0, -1):
        if not n % num and not m % num:
            break
    return [num, n*m/num]


print(solution(3, 12)) #=> [3, 12]
print(solution(2, 5)) #=> [1, 10]
