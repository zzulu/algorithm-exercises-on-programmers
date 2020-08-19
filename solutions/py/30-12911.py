def solution(n):
    count_1 = bin(n).count('1')
    n += 1
    while count_1 != bin(n).count('1'):
        n += 1
    return n


print(solution(78)) #=> 83
print(solution(15)) #=> 23
