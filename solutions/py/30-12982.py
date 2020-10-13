def solution(d, budget):
    count = 0
    for r in sorted(d):
        if r > budget:
            break
        budget -= r
        count += 1
    return count


print(solution([1, 3, 2, 5, 4], 9)) #=> 3
print(solution([2, 2, 3, 3], 10)) #=> 4
