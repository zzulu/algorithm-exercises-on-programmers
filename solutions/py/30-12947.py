def solution(x):
    s, q = 0, x
    while q:
        q, r = q // 10, q % 10
        s += r
    return False if x % s else True


print(solution(10)) #=> True
print(solution(12)) #=> True
print(solution(11)) #=> False
print(solution(13)) #=> False
