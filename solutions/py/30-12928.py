def solution(n):
    s = 0
    for num in range(1, n+1):
        if not n % num:
            s += num
    return s
    # return sum([x for x in range(1, n+1) if not n % x])


print(solution(12)) #=> 28
print(solution(5)) #=> 6
