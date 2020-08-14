def solution(n):
    numbers = [0 if x < 2 else 1 for x in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        if numbers[i]:
            for j in range(i*2, n+1, i):
                numbers[j] = 0
    return sum(numbers)


print(solution(10)) #=> 4
print(solution(5)) #=> 3
