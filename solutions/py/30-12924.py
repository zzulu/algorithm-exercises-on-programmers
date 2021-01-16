def solution(n):
    count = 0
    for i in range(1, n+1):
        s = 0
        for j in range(i, n+1):
            s += j
            if s == n:
                count += 1
                break
            if s > n:
                break
    return count


print(solution(15)) #=> 4
