def solution(n):
    return int((n**0.5+1)**2) if n**0.5 == int(n**0.5) else -1


print(solution(121)) #=> 144
print(solution(3)) #=> -1
