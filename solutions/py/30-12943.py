def solution(num):
    for n in range(500):
        if num == 1:
            return n
        num = num*3+1 if num % 2 else num / 2
    return -1


print(solution(1)) #=> 0
print(solution(6)) #=> 8
print(solution(16)) #=> 4
print(solution(626331)) #=> -1
