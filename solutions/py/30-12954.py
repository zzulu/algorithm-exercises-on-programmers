def solution(x, n):
    if x:
        return [x for x in range(x, x*(n+1), x)]
    return [x]*n


print(solution(2, 5)) #=> [2, 4, 6, 8, 10]
print(solution(4, 3)) #=> [4, 8, 12]
print(solution(-4, 2)) #=> [-4, -8]
