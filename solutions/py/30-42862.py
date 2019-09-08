def solution(n, lost, reserve):
    n_lost = [l for l in lost if not l in reserve]
    n_reserve = [r for r in reserve if not r in lost]

    for r in n_reserve:
        if r-1 in n_lost:
            n_lost.remove(r-1)
        elif r+1 in n_lost:
            n_lost.remove(r+1)

    return n - len(n_lost)


print(solution(5, [2, 4], [1, 3, 5])) #=> 5
print(solution(5, [2, 4], [3])) #=> 4
print(solution(3, [3], [1])) #=> 2
print(solution(5, [2, 3, 4], [3, 4, 5])) #=> 4
print(solution(3, [1, 2], [2, 3])) #=> 2
